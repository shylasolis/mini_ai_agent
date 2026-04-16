# Mini AI Agent

This is a small Python AI agent designed to be easy to read and easy to run.

It can:
- chat with you in the terminal
- calculate basic arithmetic
- save notes
- read back saved notes

## Why this is a good first agent

The project stays intentionally small:
- `main.py` starts the app
- `agent.py` runs the LLM loop and tool-calling logic
- `tools.py` contains the local tools

You can read the whole project in a few minutes and see how an agent works end to end.

## Setup

1. Create a Python virtual environment.
2. Install the dependencies.
3. Copy `.env.example` to `.env`.
4. Add your OpenAI API key to `.env`.
5. Run the app.

## Populate The Environment Template

1. Copy `.env.example` to `.env`.
2. Open `.env` in your editor.
3. Replace `OPENAI_API_KEY=your_api_key_here` with your real key.
4. (Optional) keep `OPENAI_MODEL=gpt-4.1-mini` or change it to another model.

Example `.env`:

```env
OPENAI_API_KEY=sk-your-real-api-key
OPENAI_MODEL=gpt-4.1-mini
```

Important:
- Do not commit `.env` to git.
- If a key is exposed, rotate/revoke it immediately.

## Commands (Windows)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python main.py
```

## Commands (macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 main.py
```

## Example prompts

- `What time is it?`
- `Calculate (24 + 18) / 3`
- `Save a note that my next project should use Streamlit`
- `Show me my notes`

## Common issues

- `401 invalid_api_key`: your `.env` file still has the wrong key or an expired key.
- `429 insufficient_quota`: your OpenAI account, project, or billing setup does not currently have API quota available.

## How the agent works

1. You type a message.
2. The model decides whether it should answer directly or call a tool.
3. If it calls a tool, Python runs that tool locally.
4. The tool result is sent back to the model.
5. The model returns a final answer.

## Next upgrades

After this works, the easiest next steps are:
- add a web UI with Streamlit
- give it a search tool
- let it read files from a chosen folder
- add memory beyond the current chat session