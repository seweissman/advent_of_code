"""
--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

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
The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.
Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
Directory d has total size 24933642.
As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
"""

from typing import Dict, List, Union

SAMPLE_INPUT = """
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
7214296 k"""


class File:
    def __init__(self, name: str, size: int = 0):
        self.name: str = name
        self.size: int = size


class Directory(File):
    def __init__(self, name: str, parent: Union["Directory", None] = None):
        super().__init__(name)
        self.contents: List[File] = []
        self.parent: Union[Directory, None] = parent


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def execute_lines(lines: List[str], dirmap: Dict[str, Directory]) -> None:
    curr_dir = dirmap["/"]
    curr_line = 0
    while curr_line < len(lines):
        line = lines[curr_line]
        print(line)
        if line.startswith("$ "):
            cmd = line[2:4]
            if cmd == "cd":
                dest = line[5:]
                if dest == "..":
                    parent_dir = curr_dir.parent
                    if parent_dir:
                        curr_dir = dirmap[parent_dir.name]
                    else:
                        raise Exception("can't cd to parent of root directory")
                else:
                    curr_dir = dirmap[dest]
                curr_line += 1
            elif cmd == "ls":
                curr_line += 1
                while curr_line < len(lines) and not lines[curr_line].startswith("$ "):
                    ls_line = lines[curr_line]
                    size_str, name = ls_line.split(" ")
                    if size_str == "dir":
                        if name not in dirmap:
                            new_dir = Directory(name, parent=curr_dir)
                            curr_dir.contents.append(new_dir)
                            dirmap[name] = new_dir
                    else:
                        size = int(size_str)
                        new_file = File(name, size=size)
                        curr_dir.contents.append(new_file)
                    curr_line += 1


def test_sample():
    lines = parse_input(SAMPLE_INPUT)
    root = Directory("/")
    dirmap = {"/": root}
    execute_lines(lines, dirmap)
    sizemap = {}
    calculate_sizes(dirmap, sizemap, root)
    assert sizemap["e"] == 584
    assert sizemap["a"] == 94853
    assert sizemap["d"] == 24933642
    assert sizemap["/"] == 48381165


def calculate_sizes(dirmap, sizemap, curr_file: File):
    if not isinstance(curr_file, Directory):
        return curr_file.size
    dir_sum = sum([calculate_sizes(dirmap, sizemap, file) for file in curr_file.contents])
    sizemap[curr_file.name] = dir_sum
    return dir_sum


if __name__ == "__main__":
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()

    lines = parse_input(input_text)
    root = Directory("/")
    dirmap = {"/": root}
    execute_lines(lines, dirmap)
    sizemap = {}
    calculate_sizes(dirmap, sizemap, root)
    print(sizemap)
    part1sum = sum([size for size in sizemap.values() if size <= 100000])
    print("Part 1: ", part1sum)