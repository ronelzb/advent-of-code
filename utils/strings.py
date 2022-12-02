from functools import wraps
from textwrap import dedent
from typing import Callable, TypeVar

T = TypeVar("T")


def parse_text_as_list(fn) -> Callable[[list[str]], T]:
    """
    Decorator which converts a text to a list of str
    """
    @wraps(fn)
    def wrapper(*args):
        text = dedent(args[0]).strip()
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
        text = dedent(args[0]).strip()
        paragraphs = [[s for s in p.splitlines()] for p in text.split("\n\n")]
        return fn(paragraphs)

    return wrapper
