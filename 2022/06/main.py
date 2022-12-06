# https://adventofcode.com/2022/day/6
from utils.files import get_input
from utils.tests import tests

TEST_1 = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
]


# Time complexity: O(n)
# Space complexity: O(1)
# Classical sliding window problem
@get_input
@tests(TEST_1)
def part_1(signal: str) -> int:
    needed_characters = 4
    start = 0
    seen = [-1] * 26

    for i, c in enumerate(signal):
        c_idx = seen[ord(c) - 97]
        if start <= c_idx:
            start = c_idx + 1

        if i - start + 1 == needed_characters:
            return i + 1

        seen[ord(c) - 97] = i

    return -1


TEST_2 = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
]


# Time complexity: O(n)
# Space complexity: O(1)
@get_input
@tests(TEST_2)
def part_2(signal: str) -> int:
    needed_characters = 14
    start = 0
    seen = [-1] * 26

    for i, c in enumerate(signal):
        c_idx = seen[ord(c) - 97]
        if start <= c_idx:
            start = c_idx + 1

        if i - start + 1 == needed_characters:
            return i + 1

        seen[ord(c) - 97] = i

    return -1


if __name__ == '__main__':
    print(part_1())
    print(part_2())
