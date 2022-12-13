# https://adventofcode.com/2022/day/13
from ast import literal_eval
from typing import List

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


TEST_1 = [
    ("""    
    [1,1,3,1,1]
    [1,1,5,1,1]
    
    [[1],[2,3,4]]
    [[1],4]
    
    [9]
    [[8,7,6]]
    
    [[4,4],4,4]
    [[4,4],4,4,4]
    
    [7,7,7,7]
    [7,7,7]
    
    []
    [3]
    
    [[[]]]
    [[]]
    
    [1,[2,[3,[4,[5,6,7]]]],8,9]
    [1,[2,[3,[4,[5,6,0]]]],8,9]
    """,
     13),
]


# Time complexity: O(m+n); m and n total length of each packet if flattened
# Space complexity: O(m+n)
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(packets: List[str]) -> int:
    indices_sum = 0

    def check_lists(a: list, b: list) -> int:
        i, j = 0, 0
        if a and not b:
            return 0
        if b and not a:
            return 1

        m, n = len(a), len(b)
        while i < m and j < n:
            if isinstance(a[i], list) and isinstance(b[j], list):
                res = check_lists(a[i], b[j])
                if res != 2:
                    return res

            if isinstance(a[i], list) and not isinstance(b[j], list):
                res = check_lists(a[i], [b[j]])
                return 0 if res == 2 else res

            if not isinstance(a[i], list) and isinstance(b[j], list):
                res = check_lists([a[i]], b[j])
                return 1 if res == 2 else res

            if a[i] != b[j]:
                return 1 if a[i] < b[j] else 0

            i += 1
            j += 1

        return 1 if m - i < n - j else (0 if m - i > n - j else 2)

    for p in range(0, len(packets), 3):
        list_a = list(literal_eval(packets[p]))
        list_b = list(literal_eval(packets[p + 1]))

        if check_lists(list_a, list_b) == 1:
            indices_sum += (p // 3 + 1)

    return indices_sum


TEST_2 = [
    ("""    
    [1,1,3,1,1]
    [1,1,5,1,1]

    [[1],[2,3,4]]
    [[1],4]

    [9]
    [[8,7,6]]

    [[4,4],4,4]
    [[4,4],4,4,4]

    [7,7,7,7]
    [7,7,7]

    []
    [3]

    [[[]]]
    [[]]

    [1,[2,[3,[4,[5,6,7]]]],8,9]
    [1,[2,[3,[4,[5,6,0]]]],8,9]
    """,
     140),
]


# Time complexity: O(p*log(p)*(m+n)); k=len(packets)
# Space complexity: O(p*(m+n))
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(packets_str: List[str]) -> int:

    def check_lists(a: list, b: list) -> int:
        i, j = 0, 0
        if a and not b:
            return 0
        if b and not a:
            return 1

        m, n = len(a), len(b)
        while i < m and j < n:
            if isinstance(a[i], list) and isinstance(b[j], list):
                res = check_lists(a[i], b[j])
                if res != 2:
                    return res

            if isinstance(a[i], list) and not isinstance(b[j], list):
                res = check_lists(a[i], [b[j]])
                return 0 if res == 2 else res

            if not isinstance(a[i], list) and isinstance(b[j], list):
                res = check_lists([a[i]], b[j])
                return 1 if res == 2 else res

            if a[i] != b[j]:
                return 1 if a[i] < b[j] else 0

            i += 1
            j += 1

        return 1 if m - i < n - j else (0 if m - i > n - j else 2)

    def quick_sort(unsorted_array):
        if len(unsorted_array) < 2:
            return unsorted_array

        pivot = unsorted_array[0]
        loe = [elem for elem in unsorted_array[1:] if check_lists(elem, pivot) > 0]  # elem <= pivot
        gt = [elem for elem in unsorted_array[1:] if check_lists(elem, pivot) == 0]  # elem > pivot

        return quick_sort(loe) + [pivot] + quick_sort(gt)

    packets = []
    for p in range(0, len(packets_str), 3):
        packets.append(list(literal_eval(packets_str[p])))
        packets.append(list(literal_eval(packets_str[p + 1])))

    packets.append([[2]])
    packets.append([[6]])

    packets = quick_sort(packets)

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
