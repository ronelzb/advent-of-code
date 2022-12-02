# https://adventofcode.com/2022/day/1
import heapq
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_paragraphs
from utils.integers import list_str_to_int
from utils.tests import tests

TESTS_1 = [
    ("""
    1000
    2000
    3000
    
    4000
    
    5000
    6000
    
    7000
    8000
    9000
    
    10000
    """,
     24000),
]


# Time complexity: O(n)
# Space complexity: O(1)
@get_input
@tests(TESTS_1)
@parse_text_as_paragraphs
def part_1(elves_calories: List[List[str]]) -> int:
    return max(sum(elf_calories) for elf_calories in list_str_to_int(elves_calories))


TESTS_2 = [
    ("""
    1000
    2000
    3000
    
    4000
    
    5000
    6000
    
    7000
    8000
    9000
    
    10000
    """,
     45000),
]


# Time complexity: O(n*log(k)) => k = 3 => O(n)
# Space complexity: O(k)
# My initial thought was to sort descending each elf total calories and grab the first 3
# But a more efficient way is to a max-heap to keep the top 3 elf calories in the iteration
@get_input
@tests(TESTS_2)
@parse_text_as_paragraphs
def part_2(elves_calories: List[List[str]]) -> int:
    heap = []
    k = 0

    for elf_calories in list_str_to_int(elves_calories):
        total_calories = sum(elf_calories)
        if k < 3:
            heapq.heappush(heap, total_calories)
            k += 1
        else:
            heapq.heappushpop(heap, total_calories)

    return sum(calories for calories in heap)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
