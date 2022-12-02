import re
from typing import List


def ints(text):
    if isinstance(text, list):
        return list(map(int, text))

    return [int(i) for i in re.findall(r'-?\d+', text)]


def list_str_to_int(str_list) -> List[List[int]]:
    return [ints(sl) for sl in str_list]
