# https://adventofcode.com/2022/day/11
import heapq
from functools import reduce
from typing import List

import attr

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


@attr.define
class Monkey:
    items: list[int] = []
    operator: str = "+"
    operand: int = 0
    divisible_by: int = 1
    next_monkey: tuple = ()
    inspected_items: int = 0

    def get_item_new_value(self, i: int) -> int:
        item = self.items[i]
        operand = self.operand if self.operand > 0 else self.items[i]

        if self.operator == "+":
            item += operand
        else:  # *
            item *= operand

        self.inspected_items += 1

        return item


TEST_1 = [
    ("""
    Monkey 0:
      Starting items: 79, 98
      Operation: new = old * 19
      Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3
    
    Monkey 1:
      Starting items: 54, 65, 75, 74
      Operation: new = old + 6
      Test: divisible by 19
        If true: throw to monkey 2
        If false: throw to monkey 0
    
    Monkey 2:
      Starting items: 79, 60, 97
      Operation: new = old * old
      Test: divisible by 13
        If true: throw to monkey 1
        If false: throw to monkey 3
    
    Monkey 3:
      Starting items: 74
      Operation: new = old + 3
      Test: divisible by 17
        If true: throw to monkey 0
        If false: throw to monkey 1
    """,
     10605),
]


# Time complexity: O(m*n + m*log(m)); m=len(monkeys), n=len(worry items)
# Space complexity: O(m*n)
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(lines: List[str]) -> int:
    monkeys = []

    for i in range(0, len(lines), 7):
        monkey = Monkey()
        monkey.items = list(map(int, lines[i + 1].split(":")[1].split(", ")))

        operation_line = lines[i + 2].split()
        monkey.operator = operation_line[-2]
        monkey.operand = int(operation_line[-1]) if operation_line[-1].isdigit() else 0

        monkey.divisible_by = int(lines[i + 3].split()[-1])
        monkey.next_monkey = (int(lines[i + 4].split()[-1]), int(lines[i + 5].split()[-1]))

        monkeys.append(monkey)

    for _ in range(20):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                new_value = monkey.get_item_new_value(i)
                new_value //= 3  # worry levels relief
                next_monkey = monkey.next_monkey[0] if new_value % monkey.divisible_by == 0 else monkey.next_monkey[1]
                monkeys[next_monkey].items.append(new_value)

            monkey.items = []

    return reduce(lambda x, y: x * y, sorted([monkey.inspected_items for monkey in monkeys], reverse=True)[:2])


TEST_2 = [
    ("""
    Monkey 0:
      Starting items: 79, 98
      Operation: new = old * 19
      Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3

    Monkey 1:
      Starting items: 54, 65, 75, 74
      Operation: new = old + 6
      Test: divisible by 19
        If true: throw to monkey 2
        If false: throw to monkey 0

    Monkey 2:
      Starting items: 79, 60, 97
      Operation: new = old * old
      Test: divisible by 13
        If true: throw to monkey 1
        If false: throw to monkey 3

    Monkey 3:
      Starting items: 74
      Operation: new = old + 3
      Test: divisible by 17
        If true: throw to monkey 0
        If false: throw to monkey 1
    """,
     2713310158),
]


# Time complexity: O(m*n + m*log(m)); m=len(monkeys), n=len(worry items)
# Space complexity: O(m*n)
# mod makes worry levels manageable: find the GCD for all monkeys' divisible by
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(lines: List[str]) -> int:
    monkeys = []

    for i in range(0, len(lines), 7):
        monkey = Monkey()
        monkey.items = list(map(int, lines[i + 1].split(":")[1].split(", ")))

        operation_line = lines[i + 2].split()
        monkey.operator = operation_line[-2]
        monkey.operand = int(operation_line[-1]) if operation_line[-1].isdigit() else 0

        monkey.divisible_by = int(lines[i + 3].split()[-1])
        monkey.next_monkey = (int(lines[i + 4].split()[-1]), int(lines[i + 5].split()[-1]))

        monkeys.append(monkey)

    mod = reduce(lambda x, y: x * y, [monkey.divisible_by for monkey in monkeys])

    for _ in range(10_000):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                new_value = monkey.get_item_new_value(i)
                new_value %= mod  # worry levels relief
                next_monkey = monkey.next_monkey[0] if new_value % monkey.divisible_by == 0 else monkey.next_monkey[1]
                monkeys[next_monkey].items.append(new_value)

            monkey.items = []

    return reduce(lambda x, y: x * y, sorted([monkey.inspected_items for monkey in monkeys], reverse=True)[:2])


if __name__ == '__main__':
    print(part_1())
    print(part_2())
