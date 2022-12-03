# https://adventofcode.com/2022/day/3
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


TEST_1 = [
    ("""
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """,
     157),
]


# Time complexity: O(n*m); n=number of rucksacks, m=each len(rucksack)
# Space complexity: O(m)
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(rucksacks: List[str]) -> int:
    total_priorities = 0

    for rucksack in rucksacks:
        half = len(rucksack) // 2
        first_comp_items = set(rucksack[:half])
        second_comp_items = set(rucksack[half:])
        common_item = str((first_comp_items & second_comp_items).pop())

        total_priorities += ord(common_item) - (96 if common_item.islower() else 38)

    return total_priorities


TEST_2 = [
    ("""
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """,
     70),
]


# Time complexity: O(n*m)
# Space complexity: O(m)
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(rucksacks: List[str]) -> int:
    total_priorities = 0

    for i in range(0, len(rucksacks), 3):
        badge = str((set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])).pop())
        total_priorities += ord(badge) - (96 if badge.islower() else 38)

    return total_priorities


if __name__ == '__main__':
    print(part_1())
    print(part_2())
