# https://adventofcode.com/2022/day/10
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests

TEST_1 = [
    ("""
    addx 15
    addx -11
    addx 6
    addx -3
    addx 5
    addx -1
    addx -8
    addx 13
    addx 4
    noop
    addx -1
    addx 5
    addx -1
    addx 5
    addx -1
    addx 5
    addx -1
    addx 5
    addx -1
    addx -35
    addx 1
    addx 24
    addx -19
    addx 1
    addx 16
    addx -11
    noop
    noop
    addx 21
    addx -15
    noop
    noop
    addx -3
    addx 9
    addx 1
    addx -3
    addx 8
    addx 1
    addx 5
    noop
    noop
    noop
    noop
    noop
    addx -36
    noop
    addx 1
    addx 7
    noop
    noop
    noop
    addx 2
    addx 6
    noop
    noop
    noop
    noop
    noop
    addx 1
    noop
    noop
    addx 7
    addx 1
    noop
    addx -13
    addx 13
    addx 7
    noop
    addx 1
    addx -33
    noop
    noop
    noop
    addx 2
    noop
    noop
    noop
    addx 8
    noop
    addx -1
    addx 2
    addx 1
    noop
    addx 17
    addx -9
    addx 1
    addx 1
    addx -3
    addx 11
    noop
    noop
    addx 1
    noop
    addx 1
    noop
    noop
    addx -13
    addx -19
    addx 1
    addx 3
    addx 26
    addx -30
    addx 12
    addx -1
    addx 3
    addx 1
    noop
    noop
    noop
    addx -9
    addx 18
    addx 1
    addx 2
    noop
    noop
    addx 9
    noop
    noop
    noop
    addx -1
    addx 2
    addx -37
    addx 1
    addx 3
    noop
    addx 15
    addx -21
    addx 22
    addx -6
    addx 1
    noop
    addx 2
    addx 1
    noop
    addx -10
    noop
    noop
    addx 20
    addx 1
    addx 2
    addx 2
    addx -6
    addx -11
    noop
    noop
    noop
    """,
     13140),
]


# Time complexity: O(k); k=len(instructions)
# Space complexity: O(1)
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(instructions: List[str]) -> int:
    cycles, x, signal_strength_index, total_signal_strength, = 1, 1, 0, 0
    next_signal_strength_cycles = [20, 60, 100, 140, 180, 220]

    for instruction in instructions:
        instruction_split = instruction.split()
        if instruction_split[0] == "addx":
            cycles += 2
            prev_x = x
            x += int(instruction_split[1])

            if cycles >= next_signal_strength_cycles[signal_strength_index]:
                signal_strength = next_signal_strength_cycles[signal_strength_index]
                total_signal_strength += (x if cycles == signal_strength else prev_x) * signal_strength
                signal_strength_index += 1
                if signal_strength_index == len(next_signal_strength_cycles):
                    break
        else:
            cycles += 1

    return total_signal_strength


TEST_2 = [
    ("""
    addx 15
    addx -11
    addx 6
    addx -3
    addx 5
    addx -1
    addx -8
    addx 13
    addx 4
    noop
    addx -1
    addx 5
    addx -1
    addx 5
    addx -1
    addx 5
    addx -1
    addx 5
    addx -1
    addx -35
    addx 1
    addx 24
    addx -19
    addx 1
    addx 16
    addx -11
    noop
    noop
    addx 21
    addx -15
    noop
    noop
    addx -3
    addx 9
    addx 1
    addx -3
    addx 8
    addx 1
    addx 5
    noop
    noop
    noop
    noop
    noop
    addx -36
    noop
    addx 1
    addx 7
    noop
    noop
    noop
    addx 2
    addx 6
    noop
    noop
    noop
    noop
    noop
    addx 1
    noop
    noop
    addx 7
    addx 1
    noop
    addx -13
    addx 13
    addx 7
    noop
    addx 1
    addx -33
    noop
    noop
    noop
    addx 2
    noop
    noop
    noop
    addx 8
    noop
    addx -1
    addx 2
    addx 1
    noop
    addx 17
    addx -9
    addx 1
    addx 1
    addx -3
    addx 11
    noop
    noop
    addx 1
    noop
    addx 1
    noop
    noop
    addx -13
    addx -19
    addx 1
    addx 3
    addx 26
    addx -30
    addx 12
    addx -1
    addx 3
    addx 1
    noop
    noop
    noop
    addx -9
    addx 18
    addx 1
    addx 2
    noop
    noop
    addx 9
    noop
    noop
    noop
    addx -1
    addx 2
    addx -37
    addx 1
    addx 3
    noop
    addx 15
    addx -21
    addx 22
    addx -6
    addx 1
    noop
    addx 2
    addx 1
    noop
    addx -10
    noop
    noop
    addx 20
    addx 1
    addx 2
    addx 2
    addx -6
    addx -11
    noop
    noop
    noop
    """,
     "##..##..##..##..##..##..##..##..##..##..\n"
     "###...###...###...###...###...###...###.\n"
     "####....####....####....####....####....\n"
     "#####.....#####.....#####.....#####.....\n"
     "######......######......######......####\n"
     "#######.......#######.......#######....."),
]


# Time complexity: O(k+6*40) => O(k)
# Space complexity: O(40*6) => O(1)
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(instructions: List[str]) -> str:
    def draw(register: int):
        pos = cycles % 40
        crt[cycles % 240] = "#" if abs(register - pos) <= 1 else "."

    cycles, x = 0, 1
    crt = ["." for _ in range(240)]

    for instruction in instructions:
        instruction_split = instruction.split()
        if instruction_split[0] == "addx":
            draw(x)
            cycles += 1
            draw(x)
            cycles += 1
            x += int(instruction_split[1])
        else:
            draw(x)
            cycles += 1

    output = []
    for i in range(0, 240, 40):
        output.append("".join(crt[i: i + 40]))
    return "\n".join(output)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
