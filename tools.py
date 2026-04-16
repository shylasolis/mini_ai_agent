from __future__ import annotations

import ast
from datetime import datetime
from pathlib import Path
from typing import Any


DATA_DIR = Path("data")
NOTES_FILE = DATA_DIR / "notes.txt"


def _ensure_data_dir() -> None:
    DATA_DIR.mkdir(exist_ok=True)


def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_note(note: str) -> str:
    _ensure_data_dir()
    cleaned_note = note.strip()
    if not cleaned_note:
        return "No note was saved because the note text was empty."

    with NOTES_FILE.open("a", encoding="utf-8") as file:
        file.write(f"- {cleaned_note}\n")

    return f"Saved note: {cleaned_note}"


def read_notes() -> str:
    _ensure_data_dir()
    if not NOTES_FILE.exists():
        return "No notes saved yet."

    content = NOTES_FILE.read_text(encoding="utf-8").strip()
    return content or "No notes saved yet."


def calculate(expression: str) -> str:
    try:
        parsed = ast.parse(expression, mode="eval")
        result = _eval_ast(parsed.body)
    except Exception as error:
        return f"Calculation failed: {error}"

    return str(result)


def _eval_ast(node: ast.AST) -> Any:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp):
        left = _eval_ast(node.left)
        right = _eval_ast(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Pow):
            return left**right
        if isinstance(node.op, ast.Mod):
            return left % right

    if isinstance(node, ast.UnaryOp):
        operand = _eval_ast(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand

    raise ValueError("Only basic arithmetic expressions are allowed.")


AVAILABLE_TOOLS = {
    "get_current_time": get_current_time,
    "save_note": save_note,
    "read_notes": read_notes,
    "calculate": calculate,
}


OPENAI_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local date and time.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "save_note",
            "description": "Save a short note for the user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "note": {
                        "type": "string",
                        "description": "The note text to save.",
                    }
                },
                "required": ["note"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_notes",
            "description": "Read all notes the user has saved so far.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a basic arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "An arithmetic expression like (12 + 3) * 4",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]