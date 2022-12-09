# https://adventofcode.com/2022/day/9
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


TEST_1 = [
    ("""
    R 4
    U 4
    L 3
    D 1
    R 4
    D 1
    L 5
    R 2
    """,
     13),
]


# Time complexity: O(m*s); m=len(motions), t=each motion steps
# Space complexity: O(1)
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(motions: List[str]) -> int:
    pos_visited = {(0, 0)}
    h, t = [0, 0], (0, 0)

    for motion in motions:
        direction, steps = motion.split()

        for _ in range(int(steps)):
            if direction == "U":
                h[0] += 1
            elif direction == "R":
                h[1] += 1
            elif direction == "D":
                h[0] -= 1
            elif direction == "L":
                h[1] -= 1

            distance = max(abs(h[0]-t[0]), abs(h[1] - t[1]))
            if distance > 1:
                if direction == "U":
                    t = (h[0] - 1, h[1])
                elif direction == "R":
                    t = (h[0], h[1] - 1)
                elif direction == "D":
                    t = (h[0] + 1, h[1])
                elif direction == "L":
                    t = (h[0], h[1] + 1)
                pos_visited.add(t)

    return len(pos_visited)


TEST_2 = [
    ("""
    R 4
    U 4
    L 3
    D 1
    R 4
    D 1
    L 5
    R 2
    """,
     1),
    ("""
    R 5
    U 8
    L 8
    D 3
    R 17
    D 10
    L 25
    U 20
    """,
     36)
]


# Time complexity: O(m*s*k); m=len(motions), t=each motion steps, k=len(knots)
# Space complexity: O(k)
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(motions: List[str]) -> int:
    pos_visited = {(0, 0)}
    knot_count = 10
    knots = [[0, 0] for _ in range(knot_count)]

    def signum(x: int) -> int:
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    for motion in motions:
        direction, steps = motion.split()

        for _ in range(int(steps)):
            if direction == "U":
                knots[0][0] += 1
            elif direction == "R":
                knots[0][1] += 1
            elif direction == "D":
                knots[0][0] -= 1
            elif direction == "L":
                knots[0][1] -= 1

            for i in range(1, knot_count):
                hx, hy = knots[i - 1]
                tx, ty = knots[i]
                dx, dy = tx - hx, ty - hy

                if abs(dx) > 1 or abs(dy) > 1:
                    knots[i][0] -= signum(dx)
                    knots[i][1] -= signum(dy)

            pos_visited.add(tuple(knots[-1]))

    return len(pos_visited)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
