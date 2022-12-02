from functools import wraps, cache
from typing import Callable, TypeVar

T = TypeVar("T")


def get_input(fn: Callable[[str], T]) -> T:
    """
    Decorator to get the raw input file content
    """
    @wraps(fn)
    def wrapper():
        input_raw_content = _get_input()
        return fn(input_raw_content)

    return wrapper


@cache
def _get_input() -> str:
    """
    Returns the puzzle file input using the folder that the script/solution is in.

    This method assumes that inside each folder there is an 'input.txt' file.
    :return: File raw content
    """
    with open("input") as reader:
        content = reader.read().strip()
    return content
