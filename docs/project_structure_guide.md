# Project Structure Guide

Use this guide to quickly identify which files belong to each version.

## Terminal baseline (Version 1)

This version lives on the `main` branch.

- [main.py](main.py): terminal entry point
- [agent.py](agent.py): terminal agent loop and API calls
- [tools.py](tools.py): shared local tools
- [requirements.txt](requirements.txt): core dependencies

## Streamlit version (Version 2)

This version lives on the `streamlit-version` branch.

- [streamlit_app/app.py](streamlit_app/app.py): Streamlit UI entry point
- [requirements_streamlit.txt](requirements_streamlit.txt): Streamlit dependencies
- [docs/terminal_vs_streamlit.md](docs/terminal_vs_streamlit.md): compare and contrast notes

## Shared files used by both

- [.env.example](.env.example): environment template for users
- [README.md](README.md): setup and run instructions

## Rule of thumb

- If the file is inside [streamlit_app/](streamlit_app), it is Streamlit-specific.
- If the file is in the project root on `main`, it is part of the terminal baseline.
- Keep shared logic in one place to avoid duplicate code.

## Branch strategy

- Keep terminal baseline on branch: main
- Keep Streamlit work on branch: streamlit-version
- Use compare view for teaching:
  https://github.com/shylasolis/mini_ai_agent/compare/main...streamlit-version