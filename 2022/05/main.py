# https://adventofcode.com/2022/day/5
from utils.files import get_input
from utils.tests import tests

TEST_1 = [
    ("""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
    
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""",
     "CMZ"),
]


# Time complexity: O(k*n); k=number of moves, n=move between stacks can be 2*n
# Space complexity: O(m*n); m=len(stacks), n=each stack
@get_input
@tests(TEST_1)
def part_1(raw: str) -> str:
    # rstrip: for input end
    raw = raw.rstrip()
    lines = raw.split("\n")
    row = 0
    stacks_len = (len(lines[0]) + 1) // 4
    stacks = [[] * 0 for _ in range(stacks_len)]

    while not lines[row][1].isdigit():
        for i in range(stacks_len):
            crate = lines[row][i * 4 + 1]
            if crate != " ":
                stacks[i].insert(0, crate)
        row += 1

    row += 2
    while row < len(lines):
        line_split = lines[row].split()
        crates_to_move, stack_from, stack_to = int(line_split[1]), int(line_split[3]) - 1, int(line_split[5]) - 1
        stack_from_len = len(stacks[stack_from])

        aux = stacks[stack_from][stack_from_len - crates_to_move:]
        del stacks[stack_from][stack_from_len - crates_to_move:]
        stacks[stack_to].extend(aux[::-1])

        row += 1

    return "".join([stack[-1] for stack in stacks])


TEST_2 = [
    ("""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""",
     "MCD"),
]


# Time complexity: O(k*n)
# Space complexity: O(m*n)
@get_input
@tests(TEST_2)
def part_2(raw: str) -> str:
    # rstrip: for input end
    raw = raw.rstrip()
    lines = raw.split("\n")
    row = 0
    stacks_len = (len(lines[0]) + 1) // 4
    stacks = [[] * 0 for _ in range(stacks_len)]

    while not lines[row][1].isdigit():
        for i in range(stacks_len):
            crate = lines[row][i * 4 + 1]
            if crate != " ":
                stacks[i].insert(0, crate)
        row += 1

    row += 2
    while row < len(lines):
        line_split = lines[row].split()
        crates_to_move, stack_from, stack_to = int(line_split[1]), int(line_split[3]) - 1, int(line_split[5]) - 1
        stack_from_len = len(stacks[stack_from])

        aux = stacks[stack_from][stack_from_len - crates_to_move:]
        del stacks[stack_from][stack_from_len - crates_to_move:]
        stacks[stack_to].extend(aux)

        row += 1

    return "".join([stack[-1] for stack in stacks])


if __name__ == '__main__':
    print(part_1())
    print(part_2())
