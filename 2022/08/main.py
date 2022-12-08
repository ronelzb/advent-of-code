# https://adventofcode.com/2022/day/8
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


TEST_1 = [
    ("""
    30373
    25512
    65332
    33549
    35390
    """,
     21),
]


# Time complexity:O(m*n*(m + n))
# Space complexity: O(m*n)
# Traverse the grid solution spiral clockwise from outside to the center
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(lines: List[str]) -> int:
    def _check_if_visible(x: int, y: int) -> bool:
        dx = x - 1
        while dx >= 0 and grid[dx][y] < grid[x][y]:
            dx -= 1
        if dx == -1: return True

        dx = x + 1
        while dx < m and grid[dx][y] < grid[x][y]:
            dx += 1
        if dx == m: return True

        dy = y - 1
        while dy >= 0 and grid[x][dy] < grid[x][y]:
            dy -= 1
        if dy == -1: return True

        dy = y + 1
        while dy < n and grid[x][dy] < grid[x][y]:
            dy += 1
        if dy == n: return True

        return False

    m, n = len(lines), len(lines[0])
    grid = [[] * 0 for _ in range(m)]
    total_visible = 0

    for i, line in enumerate(lines):
        grid[i] = list(map(int, line))

    for i in range(m):
        total_visible += (2 if n > 1 else 1)
    for j in range(1, n - 1):
        total_visible += (2 if m > 1 else 1)

    top, bottom = 1, m - 2
    left, right = 1, n - 2

    while top <= bottom and left <= right:
        for x in range(left, right + 1):
            if _check_if_visible(top, x):
                total_visible += 1
        top += 1

        for y in range(top, bottom + 1):
            if _check_if_visible(y, right):
                total_visible += 1
        right -= 1

        for x in range(right, left - 1, -1):
            if bottom < top: break
            if _check_if_visible(bottom, x):
                total_visible += 1
        bottom -= 1

        for y in range(bottom, top - 1, -1):
            if right < left: break
            if _check_if_visible(y, left):
                total_visible += 1
        left += 1

    return total_visible


TEST_2 = [
    ("""
    30373
    25512
    65332
    33549
    35390
    """,
     8),
]


# Time complexity: O(m*n*(m+n))
# Space complexity: O(m*n)
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(lines: List[str]) -> int:
    def _calculate_scenic_score(x: int, y: int) -> int:
        view_left = 1
        while x - view_left > 0 and grid[x - view_left][y] < grid[x][y]:
            view_left += 1

        view_right = 1
        while x + view_right < m - 1 and grid[x + view_right][y] < grid[x][y]:
            view_right += 1

        view_top = 1
        while y - view_top > 0 and grid[x][y - view_top] < grid[x][y]:
            view_top += 1

        view_bottom = 1
        while y + view_bottom < n - 1 and grid[x][y + view_bottom] < grid[x][y]:
            view_bottom += 1

        return view_left * view_right * view_top * view_bottom

    m, n = len(lines), len(lines[0])
    grid = [[] * 0 for _ in range(m)]
    max_scenic_score = 0

    for i, line in enumerate(lines):
        grid[i] = list(map(int, line))

    top, bottom = 1, m - 2
    left, right = 1, n - 2

    while top <= bottom and left <= right:
        for x in range(left, right + 1):
            max_scenic_score = max(max_scenic_score, _calculate_scenic_score(top, x))
        top += 1

        for y in range(top, bottom + 1):
            max_scenic_score = max(max_scenic_score, _calculate_scenic_score(y, right))
        right -= 1

        for x in range(right, left - 1, -1):
            if bottom < top: break
            max_scenic_score = max(max_scenic_score, _calculate_scenic_score(bottom, x))
        bottom -= 1

        for y in range(bottom, top - 1, -1):
            if right < left: break
            max_scenic_score = max(max_scenic_score, _calculate_scenic_score(y, left))
        left += 1

    return max_scenic_score


if __name__ == '__main__':
    print(part_1())
    print(part_2())
