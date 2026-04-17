# Mini AI Agent

This branch contains the Streamlit version of the Mini AI Agent.

## Branch note

You are viewing the `streamlit-version` branch.

This branch is focused on the browser-based implementation.

If you want the original terminal-only baseline, switch to the `main` branch, which contains the first version of the project.

## What is in this branch

- Streamlit app: `streamlit_app/app.py`
- Shared tools: `tools.py`
- Base dependencies: `requirements.txt`
- Streamlit dependencies: `requirements_streamlit.txt`
- Compare guide: `docs/terminal_vs_streamlit.md`

It can:
- chat with you in the browser
- calculate basic arithmetic
- save notes
- read back saved notes

## Why this is a good second step

This version shows how the same agent idea can move from a terminal UI to a browser UI.

The project stays intentionally small:
- `streamlit_app/app.py` runs the Streamlit interface and model loop
- `tools.py` contains the local tools
- `docs/terminal_vs_streamlit.md` explains what changed from the terminal version

You can read the whole project in a few minutes and see how the interface changed without changing the core agent idea.

## Setup

1. Create a Python virtual environment.
2. Install the dependencies.
3. Copy `.env.example` to `.env`.
4. Add your OpenAI API key to `.env`.
5. Run the Streamlit app.

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
pip install -r requirements_streamlit.txt
Copy-Item .env.example .env
streamlit run streamlit_app/app.py
```

## Commands (macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_streamlit.txt
cp .env.example .env
python3 -m streamlit run streamlit_app/app.py
```

## Example prompts

- `What time is it?`
- `Calculate (24 + 18) / 3`
- `Save a note that this Streamlit app works`
- `Show me my notes`

## Common issues

- `401 invalid_api_key`: your `.env` file still has the wrong key or an expired key.
- `429 insufficient_quota`: your OpenAI account, project, or billing setup does not currently have API quota available.

## How the agent works

1. You type a message in the Streamlit chat box.
2. The model decides whether it should answer directly or call a tool.
3. If it calls a tool, Python runs that tool locally.
4. The tool result is sent back to the model.
5. The model returns a final answer.

## Version organization

See [docs/project_structure_guide.md](docs/project_structure_guide.md) for a quick map of how the Streamlit branch relates to the original terminal baseline on `main`.

## Next upgrades

After this works, the easiest next steps are:
- add file upload and file reading in the web UI
- give it a search tool
- let it read files from a chosen folder
- add memory beyond the current chat session

## Contributing

Contributions are welcome, especially from beginner programmers.

### 60-second student setup checklist

1. Fork this repo.
2. Clone your fork.
3. Create and activate a virtual environment.
4. Install dependencies from `requirements_streamlit.txt`.
5. Copy `.env.example` to `.env` and add your own API key.
6. Run `streamlit run streamlit_app/app.py` (Windows) or `python3 -m streamlit run streamlit_app/app.py` (macOS).

### Contribution flow

1. Create a feature branch.
2. Make a small, focused change.
3. Test by running the Streamlit app and trying at least one prompt.
4. Commit with a clear message.
5. Open a pull request with what changed and why.