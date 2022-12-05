"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?



"""

import re
from collections import deque
from typing import List, Tuple

SAMPLE_INPUT = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

SAMPLE_START = ["ZN", "MCD", "P"]


class Stacks:
    def __init__(self, stack_list: List[str]):
        self.stacks = []
        for stack in stack_list:
            stack_que = deque()
            for crate in stack:
                stack_que.append(crate)
            self.stacks.append(stack_que)

    def move_crates(self, n: int, start_row: int, finish_row: int) -> None:
        for _ in range(n):
            crate = self.stacks[start_row - 1].pop()
            self.stacks[finish_row - 1].append(crate)

    def pop(self, n: int) -> str:
        if len(self.stacks[n - 1]) > 0:
            return self.stacks[n - 1].pop()
        return ""

    def peek(self) -> List[str]:
        return [s[-1] if len(s) > 0 else "" for s in self.stacks]

    def run_moves(self, move_list: List[Tuple[int, int, int]]) -> None:
        for move in move_list:
            self.move_crates(*move)


class Stacks9001(Stacks):
    def move_crates(self, n: int, start_row: int, finish_row: int) -> None:
        append_crates = []
        for _ in range(n):
            crate = self.stacks[start_row - 1].pop()
            append_crates.append(crate)
        for crate in reversed(append_crates):
            self.stacks[finish_row - 1].append(crate)


def test_stacks():
    stacks = Stacks(SAMPLE_START)
    assert stacks.peek() == ["N", "D", "P"]
    assert stacks.pop(1) == "N"
    assert stacks.pop(1) == "Z"


def test_moves_part1():
    stacks = Stacks(SAMPLE_START)
    # move 1 from 2 to 1
    stacks.move_crates(1, 2, 1)
    assert stacks.peek() == ["D", "C", "P"]

    # move 3 from 1 to 3
    stacks.move_crates(3, 1, 3)
    assert stacks.peek() == ["", "C", "Z"]

    # move 2 from 2 to 1
    stacks.move_crates(2, 2, 1)
    assert stacks.peek() == ["M", "", "Z"]

    # move 1 from 1 to 2
    stacks.move_crates(1, 1, 2)
    assert stacks.peek() == ["C", "M", "Z"]


def test_moves_part2():
    stacks = Stacks9001(SAMPLE_START)
    # move 1 from 2 to 1
    stacks.move_crates(1, 2, 1)
    assert stacks.peek() == ["D", "C", "P"]

    # move 3 from 1 to 3
    stacks.move_crates(3, 1, 3)
    assert stacks.peek() == ["", "C", "D"]

    # move 2 from 2 to 1
    stacks.move_crates(2, 2, 1)
    assert stacks.peek() == ["C", "", "D"]

    # move 1 from 1 to 2
    stacks.move_crates(1, 1, 2)
    assert stacks.peek() == ["M", "C", "D"]


def test_run_moves_part1():
    stacks = Stacks(SAMPLE_START)
    moves = parse_input(SAMPLE_INPUT)
    stacks.run_moves(moves)
    final_state = stacks.peek()
    assert final_state == ["C", "M", "Z"]


def test_run_moves_part2():
    stacks = Stacks9001(SAMPLE_START)
    moves = parse_input(SAMPLE_INPUT)
    stacks.run_moves(moves)
    final_state = stacks.peek()
    assert final_state == ["M", "C", "D"]


PUZZLE_START = ["ZJG", "QLRPWFVC", "FPMCLGR", "LFBWPHM", "GCFSVQ", "WHJZMQTL", "HFSBV", "FJZS", "MCDPFHBT"]
"""
    [C]             [L]         [T]
    [V] [R] [M]     [T]         [B]
    [F] [G] [H] [Q] [Q]         [H]
    [W] [L] [P] [V] [M] [V]     [F]
    [P] [C] [W] [S] [Z] [B] [S] [P]
[G] [R] [M] [B] [F] [J] [S] [Z] [D]
[J] [L] [P] [F] [C] [H] [F] [J] [C]
[Z] [Q] [F] [L] [G] [W] [H] [F] [M]
 1   2   3   4   5   6   7   8   9 
"""


def parse_move(move_txt: str) -> Tuple[int, int, int]:
    m = re.match(r"move (\d+) from (\d+) to (\d+)", move_txt)
    if m is None:
        raise Exception("failed to parse move")
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def test_parse_move():
    move = parse_move("move 1 from 2 to 1")
    assert move == (1, 2, 1)

def parse_input(text: str) -> List[Tuple[int, int, int]]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    moves = [parse_move(line) for line in lines]
    return moves


if __name__ == "__main__":
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    moves = parse_input(input_text)
    stacks = Stacks(PUZZLE_START)
    stacks.run_moves(moves)
    print("Part 1", "".join(stacks.peek()))

    stacks = Stacks9001(PUZZLE_START)
    stacks.run_moves(moves)
    print("Part 2", "".join(stacks.peek()))