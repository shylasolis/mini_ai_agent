from __future__ import annotations

import json
import os

import streamlit as st
from dotenv import load_dotenv
from openai import APIConnectionError, AuthenticationError, OpenAI, OpenAIError, RateLimitError

from tools import AVAILABLE_TOOLS, OPENAI_TOOLS


SYSTEM_PROMPT = (
    "You are a helpful beginner-friendly AI agent. "
    "Use tools when they make the answer more accurate or useful. "
    "When a user asks to save or review notes, use the note tools. "
    "When a user asks for arithmetic, use the calculator tool. "
    "Keep answers short and practical."
)


def _init_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]


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


def main() -> None:
    load_dotenv()
    st.set_page_config(page_title="Mini AI Agent (Streamlit)", page_icon="🤖", layout="centered")

    st.title("Mini AI Agent: Streamlit Version")
    st.caption("This is Version 2 for compare/contrast with the terminal baseline.")

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        st.error("OPENAI_API_KEY is missing. Copy .env.example to .env and add your key.")
        st.stop()

    _init_state()

    for item in st.session_state.messages:
        if item["role"] == "user":
            with st.chat_message("user"):
                st.markdown(str(item["content"]))
        elif item["role"] == "assistant" and item.get("content"):
            with st.chat_message("assistant"):
                st.markdown(str(item["content"]))

    prompt = st.chat_input("Ask something. Example: What time is it?")
    if not prompt:
        return

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        client = OpenAI(api_key=api_key)
        try:
            reply = _complete_turn(client, model, st.session_state.messages)
            st.markdown(reply)
        except AuthenticationError:
            st.error("Your OpenAI API key was rejected. Check OPENAI_API_KEY in .env.")
        except RateLimitError:
            st.error("Your OpenAI account does not have available API quota right now.")
        except APIConnectionError:
            st.error("Could not reach OpenAI API. Check your internet connection.")
        except OpenAIError as error:
            st.error(f"OpenAI API error: {error}")


if __name__ == "__main__":
    main()