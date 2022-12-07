# https://adventofcode.com/2022/day/7
import sys
from collections import deque
from typing import List, Any

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


class FileSystem:
    def __init__(self, is_dir: bool = True, size: int = 0, parent: Any = None):
        self.is_dir = is_dir
        self.size = size
        self.parent = parent
        self.children = dict()


TEST_1 = [
    ("""
    $ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k
    """,
     95437),
]


# Time complexity: cd=O(1); dir=O(1); create file=O(log(n)); BFS=O(n) => O(n)
# Space complexity: O(n); n=number of files and folders
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(commands: List[str]) -> int:
    max_dir_size = 100000
    total_size = 0

    root = FileSystem()
    root.children["/"] = FileSystem()
    current = root.children["/"]

    for command in commands:
        if command.startswith("$ cd"):
            change_dir = command.split()[2]
            if change_dir == "/":
                current = root.children["/"]
            elif change_dir == "..":
                current = current.parent
            else:
                current = current.children[change_dir]
        elif command.startswith("dir"):
            new_dir = command.split()[1]
            if new_dir not in current.children:
                current.children[new_dir] = FileSystem(parent=current)
        elif command.split()[0].isdigit():
            file_size, filename = command.split()
            if filename not in current.children:
                current.children[filename] = FileSystem(is_dir=False, size=int(file_size), parent=current)

            c = current
            while c:
                c.size += int(file_size)
                c = c.parent

    queue = deque([root.children["/"]])
    while queue:
        current = queue.popleft()
        if current.size < max_dir_size:
            total_size += current.size

        for child in current.children:
            if current.children[child].is_dir:
                queue.append(current.children[child])

    return total_size


TEST_2 = [
    ("""
    $ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k
    """,
     24933642),
]


# Time complexity: cd=O(1); dir=O(1); create file=O(log(n)); BFS=O(n) => O(n)
# Space complexity: O(n); n=number of files and folders
@get_input
@tests(TEST_2)
@parse_text_as_list
def part_2(commands: List[str]) -> int:
    disk_space = 70000000
    min_unused_space = 30000000
    smallest_size = sys.maxsize

    root = FileSystem()
    root.children["/"] = FileSystem()
    current = root.children["/"]

    for command in commands:
        if command.startswith("$ cd"):
            change_dir = command.split()[2]
            if change_dir == "/":
                current = root.children["/"]
            elif change_dir == "..":
                current = current.parent
            else:
                current = current.children[change_dir]
        elif command.startswith("dir"):
            new_dir = command.split()[1]
            if new_dir not in current.children:
                current.children[new_dir] = FileSystem(parent=current)
        elif command.split()[0].isdigit():
            file_size, filename = command.split()
            if filename not in current.children:
                current.children[filename] = FileSystem(is_dir=False, size=int(file_size), parent=current)

            c = current
            while c:
                c.size += int(file_size)
                c = c.parent

    target_unused_space = min_unused_space - (disk_space - root.children["/"].size)
    queue = deque([root.children["/"]])
    while queue:
        current = queue.popleft()

        if current.size >= target_unused_space:
            smallest_size = min(smallest_size, current.size)

        for child in current.children:
            if current.children[child].is_dir:
                queue.append(current.children[child])

    return smallest_size


if __name__ == '__main__':
    print(part_1())
    print(part_2())
