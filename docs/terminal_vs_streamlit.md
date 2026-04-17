# Terminal vs Streamlit: Teaching Comparison

This repository now supports two versions of the same AI agent idea:

1. Terminal baseline on branch `main`
2. Streamlit UI version on branch `streamlit-version`

## Why use this for teaching

Students can compare the exact same core agent concept in two interfaces:
- command-line interaction
- browser interaction

The core ideas stay the same:
- user sends prompt
- model decides if a tool is needed
- Python runs tool locally
- model returns final answer

## What changed from terminal to Streamlit

- Terminal-only files remain on `main`.
- Input/output loop changed from `input()` and `print()` to `st.chat_input()` and `st.chat_message()`.
- Conversation history moved to `st.session_state.messages`.
- Error messages now render in UI using `st.error(...)`.
- App entry point is `streamlit_app/app.py`.

## What stayed conceptually the same

- OpenAI Chat Completions call pattern
- Tool schema (`OPENAI_TOOLS`)
- Tool execution map (`AVAILABLE_TOOLS`)
- Multi-step tool-call loop until final answer

## How students run each version

### Terminal version (main branch)

```powershell
git switch main
python main.py
```

### Streamlit version (streamlit-version branch)

Install Streamlit dependency first:

```powershell
git switch streamlit-version
pip install -r requirements_streamlit.txt
```

Then run:

```powershell
streamlit run streamlit_app/app.py
```

On macOS:

```bash
python3 -m pip install -r requirements_streamlit.txt
python3 -m streamlit run streamlit_app/app.py
```

## GitHub compare view

After pushing `streamlit-version`, compare branches on GitHub:

`https://github.com/shylasolis/mini_ai_agent/compare/main...streamlit-version`

This view is great for showing students exactly what code changed during UI migration.