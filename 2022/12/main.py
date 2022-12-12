# https://adventofcode.com/2022/day/12
import sys
from collections import deque
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


TEST_1 = [
    ("""
    Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi
    """,
     31),
]


# Time complexity: O(m*n)
# Space complexity: O(m*n)
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(grid: List[str]) -> int:
    m, n = len(grid), len(grid[0])
    start = ()
    queue = deque()
    visited = set()
    constant_elevations = {"S": "a", "E": "z"}

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                start = (i, j)

    queue.append((*start, 0))

    while queue:
        x, y, steps = queue.popleft()
        if grid[x][y] == "E":
            return steps
        visited.add((x, y))

        for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited:
                current_elevation = grid[x][y]
                if current_elevation in constant_elevations:
                    current_elevation = constant_elevations[current_elevation]

                next_elevation = grid[dx][dy]
                if next_elevation in constant_elevations:
                    next_elevation = constant_elevations[next_elevation]

                if ord(next_elevation) - ord(current_elevation) < 2:
                    visited.add((dx, dy))
                    queue.append((dx, dy, steps + 1))

    return -1


TEST_2 = [
    ("""
    Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi
    """,
     29),
]


# Time complexity: O(k*m*n); => k=number of coordinates with the lowest elevation a
# Space complexity: O(m*n)
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(grid: List[str]) -> int:
    m, n = len(grid), len(grid[0])
    starts = []

    constant_elevations = {"S": "a", "E": "z"}
    min_steps = sys.maxsize

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S" or grid[i][j] == "a":
                starts.append((i, j))

    while starts:
        start_x, start_y = starts.pop()
        queue = deque([(start_x, start_y, 0)])
        visited = set()

        while queue:
            x, y, steps = queue.popleft()
            if grid[x][y] == "E":
                min_steps = min(min_steps, steps)
                break

            visited.add((x, y))

            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited:
                    current_elevation = grid[x][y]
                    if current_elevation in constant_elevations:
                        current_elevation = constant_elevations[current_elevation]

                    next_elevation = grid[dx][dy]
                    if next_elevation in constant_elevations:
                        next_elevation = constant_elevations[next_elevation]

                    if ord(next_elevation) - ord(current_elevation) < 2:
                        visited.add((dx, dy))
                        queue.append((dx, dy, steps + 1))

    return min_steps


if __name__ == '__main__':
    print(part_1())
    print(part_2())
