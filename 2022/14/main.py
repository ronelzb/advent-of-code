# https://adventofcode.com/2022/day/14
import sys
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


TEST_1 = [
    ("""
    498,4 -> 498,6 -> 496,6
    503,4 -> 502,4 -> 502,9 -> 494,9
    """,
     24),
]


# Time complexity: O(p*m*n); p=path
# Space complexity: O(m*n)
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(paths: List[str]) -> int:
    min_x, max_x, min_y, max_y = sys.maxsize, 0, 0, 0
    for path in paths:
        coordinates = path.split(" -> ")
        for coord in coordinates:
            x, y = map(int, coord.split(","))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    cave = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for path in paths:
        coordinates = path.split(" -> ")
        for i in range(1, len(coordinates)):
            prev_x, prev_y = map(int, coordinates[i - 1].split(","))
            x, y = map(int, coordinates[i].split(","))

            if x < prev_x:
                x, prev_x = prev_x, x
            if y < prev_y:
                y, prev_y = prev_y, y
            for dx in range(prev_x, x + 1):
                for dy in range(prev_y, y + 1):
                    cave[dy - min_y][dx - min_x] = "#"

    sand_units = 0
    overflow_sand = False
    while not overflow_sand:
        sand_x, sand_y = 500, 0
        comes_to_rest = False

        while not comes_to_rest:
            dy, dx = sand_y - min_y, sand_x - min_x
            if sand_y < max_y and cave[dy + 1][dx] == ".":
                sand_y += 1
                continue
            if sand_y < max_y and sand_x > min_x and cave[dy + 1][dx - 1] == ".":
                sand_x -= 1
                sand_y += 1
                continue
            if sand_y < max_y and sand_x < max_x and cave[dy + 1][dx + 1] == ".":
                sand_x += 1
                sand_y += 1
                continue

            if sand_y == max_y or sand_x == min_x or sand_x == max_x:
                overflow_sand = True
                break

            cave[dy][dx] = "o"
            sand_units += 1
            comes_to_rest = True

    return sand_units


TEST_2 = [
    ("""
    498,4 -> 498,6 -> 496,6
    503,4 -> 502,4 -> 502,9 -> 494,9
    """,
     93),
]


# Time complexity: O(?); p*m*n + 2^m*n maybe
# Space complexity: O(?); m*2^n maybe
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(paths: List[str]) -> int:
    min_x, max_x, min_y, max_y = sys.maxsize, 0, 0, 0
    for path in paths:
        coordinates = path.split(" -> ")
        for coord in coordinates:
            x, y = map(int, coord.split(","))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    max_y += 2
    cave = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for j in range(max_x - min_x + 1):
        cave[max_y][j] = "#"

    for path in paths:
        coordinates = path.split(" -> ")
        for i in range(1, len(coordinates)):
            prev_x, prev_y = map(int, coordinates[i - 1].split(","))
            x, y = map(int, coordinates[i].split(","))

            if x < prev_x:
                x, prev_x = prev_x, x
            if y < prev_y:
                y, prev_y = prev_y, y
            for dx in range(prev_x, x + 1):
                for dy in range(prev_y, y + 1):
                    cave[dy - min_y][dx - min_x] = "#"

    sand_units = 0
    rest_starting_point = False
    while not rest_starting_point:
        sand_x, sand_y = 500, 0
        comes_to_rest = False

        while not comes_to_rest:
            dy, dx = sand_y - min_y, sand_x - min_x
            if cave[dy + 1][dx] == ".":
                sand_y += 1
                continue

            if sand_x == min_x:
                for i in range(max_y - min_y + 1):
                    cave[i].insert(0, "." if i < max_y - min_y else "#")
                min_x -= 1

            if cave[dy + 1][dx - 1] == ".":
                sand_x -= 1
                sand_y += 1
                continue

            if sand_x == max_x:
                for i in range(max_y - min_y + 1):
                    cave[i].append("." if i < max_y - min_y else "#")
                max_x += 1

            if cave[dy + 1][dx + 1] == ".":
                sand_x += 1
                sand_y += 1
                continue

            cave[dy][dx] = "o"
            sand_units += 1
            comes_to_rest = True
            if sand_x == 500 and sand_y == 0:
                rest_starting_point = True

    return sand_units


if __name__ == '__main__':
    print(part_1())
    print(part_2())
