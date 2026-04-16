from __future__ import annotations

import json
import os

from dotenv import load_dotenv
from openai import APIConnectionError, AuthenticationError, OpenAI, OpenAIError, RateLimitError

from tools import AVAILABLE_TOOLS, OPENAI_TOOLS


SYSTEM_PROMPT = """
You are a helpful beginner-friendly AI agent.
Use tools when they make the answer more accurate or useful.
When a user asks to save or review notes, use the note tools.
When a user asks for arithmetic, use the calculator tool.
Keep answers short and practical.
""".strip()


def run_agent() -> None:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        print("OPENAI_API_KEY is missing.")
        print("Create a .env file or set the environment variable before running the agent.")
        return

    client = OpenAI(api_key=api_key)
    messages: list[dict[str, object]] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    print("Mini AI Agent")
    print("Type 'exit' to stop.")

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye.")
            return

        messages.append({"role": "user", "content": user_input})
        try:
            reply = _complete_turn(client, model, messages)
        except AuthenticationError:
            print("Agent: Your OpenAI API key was rejected. Check the OPENAI_API_KEY value in .env.")
            return
        except RateLimitError:
            print("Agent: Your OpenAI account does not have available API quota right now.")
            print("Agent: Check your OpenAI billing, usage limits, or project quota, then try again.")
            return
        except APIConnectionError:
            print("Agent: I could not reach the OpenAI API. Check your internet connection and try again.")
            return
        except OpenAIError as error:
            print(f"Agent: The OpenAI API returned an error: {error}")
            return

        print(f"Agent: {reply}")


def _complete_turn(client: OpenAI, model: str, messages: list[dict[str, object]]) -> str:
    while True:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=OPENAI_TOOLS,
            tool_choice="auto",
        )

        message = response.choices[0].message
        tool_calls = message.tool_calls or []

        assistant_message: dict[str, object] = {
            "role": "assistant",
            "content": message.content or "",
        }
        if tool_calls:
            assistant_message["tool_calls"] = [call.model_dump() for call in tool_calls]
        messages.append(assistant_message)

        if not tool_calls:
            return str(message.content or "I do not have a response.")

        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments or "{}")
            tool = AVAILABLE_TOOLS[tool_name]
            tool_result = tool(**tool_args)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(tool_result),
                }
            )