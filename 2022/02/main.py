# https://adventofcode.com/2022/day/2
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


TEST_1 = [
    ("""
    A Y
    B X
    C Z
    """,
     15),
]


# Time complexity: O(n)
# Space complexity: O(1)
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(moves: List[str]) -> int:
    opponent_shape_score = {"A": 1, "B": 2, "C": 3}
    my_shape_score = {"X": 1, "Y": 2, "Z": 3}
    total_score = 0

    for move in moves:
        opponent_move, my_move = move.split()
        opponent_score, my_score = opponent_shape_score[opponent_move], my_shape_score[my_move]

        if my_score == (opponent_score % 3) + 1:
            total_score += 6
        elif my_score == opponent_score:
            total_score += 3

        total_score += my_score

    return total_score


TEST_2 = [
    ("""
    A Y
    B X
    C Z
    """,
     12),
]


# Time complexity: O(n)
# Space complexity: O(1)
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(moves: List[str]) -> int:
    opponent_shape_score = {"A": 1, "B": 2, "C": 3}
    total_score = 0

    for move in moves:
        opponent_move, outcome = move.split()
        opponent_score = opponent_shape_score[opponent_move]

        if outcome == "X":  # lose
            my_score = (3 if opponent_score == 1 else opponent_score - 1)
        elif outcome == "Y":  # draw
            my_score = opponent_score
            total_score += 3
        else:  # win
            my_score = (opponent_score % 3) + 1
            total_score += 6

        total_score += my_score

    return total_score


if __name__ == '__main__':
    print(part_1())
    print(part_2())
