import sys
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def parse_text_as_list(fn) -> Callable[[list[str]], T]:
    """
    Decorator which converts a text to a list of str
    """
    @wraps(fn)
    def wrapper(*args):
        text = trim(args[0])
        input_list = [line for line in text.split("\n")]
        return fn(input_list)

    return wrapper


def parse_text_as_paragraphs(fn) -> Callable[[list[list[str]]], T]:
    """
    Decorator which converts a text to a list(list(str)),
    which means a new list of str will be created when an empty space in a line is found
    """
    @wraps(fn)
    def wrapper(*args):
        text = trim(args[0])
        paragraphs = [[s for s in p.splitlines()] for p in text.split("\n\n")]
        return fn(paragraphs)

    return wrapper


def trim(raw: str) -> str:
    if not raw:
        return ""

    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines
    lines = raw.expandtabs().splitlines()

    # check if first line is empty (following docstring postprocessing PEP 257)
    first_line_is_empty = not lines[0].strip()

    # Determine minimum indentation (first line doesn't count if empty)
    start_line = 1 if first_line_is_empty else 0

    indent = sys.maxsize
    for line in lines[start_line:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))

    # Remove indentation
    first_line = lines[0].strip() if first_line_is_empty else lines[0][indent:]

    trimmed = [first_line]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:])

    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)

    # Return a single string:
    return "\n".join(trimmed)
