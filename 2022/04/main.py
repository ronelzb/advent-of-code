# https://adventofcode.com/2022/day/4
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests

TEST_1 = [
    ("""
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """,
     2),
]


# Time complexity: O(n)
# Space complexity: O(1)
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(assignments: List[str]) -> int:
    pairs_fully_contained = 0

    for assignment in assignments:
        first_range_str, second_range_str = assignment.split(",")
        a = tuple(map(int, first_range_str.split("-")))
        b = tuple(map(int, second_range_str.split("-")))

        if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
            pairs_fully_contained += 1

    return pairs_fully_contained


TEST_2 = [
    ("""
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """,
     4),
]


# Time complexity: O(n)
# Space complexity: O(1)
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(assignments: List[str]) -> int:
    pairs_partially_contained = 0

    for assignment in assignments:
        first_range_str, second_range_str = assignment.split(",")
        a = tuple(map(int, first_range_str.split("-")))
        b = tuple(map(int, second_range_str.split("-")))

        if a[0] <= b[1] and a[1] >= b[0]:
            pairs_partially_contained += 1

    return pairs_partially_contained


if __name__ == '__main__':
    print(part_1())
    print(part_2())
