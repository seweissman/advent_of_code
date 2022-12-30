"""
--- Day 23: Unstable Diffusion ---
You enter a large crater of gray dirt where the grove is supposed to be. All around you, plants you imagine were expected to be full of fruit are instead withered and broken. A large group of Elves has formed in the middle of the grove.

"...but this volcano has been dormant for months. Without ash, the fruit can't grow!"

You look up to see a massive, snow-capped mountain towering above you.

"It's not like there are other active volcanoes here; we've looked everywhere."

"But our scanners show active magma flows; clearly it's going somewhere."

They finally notice you at the edge of the grove, your pack almost overflowing from the random star fruit you've been collecting. Behind you, elephants and monkeys explore the grove, looking concerned. Then, the Elves recognize the ash cloud slowly spreading above your recent detour.

"Why do you--" "How is--" "Did you just--"

Before any of them can form a complete question, another Elf speaks up: "Okay, new plan. We have almost enough fruit already, and ash from the plume should spread here eventually. If we quickly plant new seedlings now, we can still make it to the extraction point. Spread out!"

The Elves each reach into their pack and pull out a tiny plant. The plants rely on important nutrients from the ash, so they can't be planted too close together.

There isn't enough time to let the Elves figure out where to plant the seedlings themselves; you quickly scan the grove (your puzzle input) and note their positions.

For example:

....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
The scan shows Elves # and empty ground .; outside your scan, more empty ground extends a long way in every direction. The scan is oriented so that north is up; orthogonal directions are written N (north), S (south), W (west), and E (east), while diagonal directions are written NE, NW, SE, SW.

The Elves follow a time-consuming process to figure out where they should each go; you can speed up this process considerably. The process consists of some number of rounds during which Elves alternate between considering where to move and actually moving.

During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:

If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.

Finally, at the end of the round, the first direction the Elves considered is moved to the end of the list of directions. For example, during the second round, the Elves would try proposing a move to the south first, then west, then east, then north. On the third round, the Elves would first consider west, then east, then north, then south.

As a smaller example, consider just these five Elves:

.....
..##.
..#..
.....
..##.
.....
The northernmost two Elves and southernmost two Elves all propose moving north, while the middle Elf cannot move north and proposes moving south. The middle Elf proposes the same destination as the southwest Elf, so neither of them move, but the other three do:

..##.
.....
..#..
...#.
..#..
.....
Next, the northernmost two Elves and the southernmost Elf all propose moving south. Of the remaining middle two Elves, the west one cannot move south and proposes moving west, while the east one cannot move south or west and proposes moving east. All five Elves succeed in moving to their proposed positions:

.....
..##.
.#...
....#
.....
..#..
Finally, the southernmost two Elves choose not to move at all. Of the remaining three Elves, the west one proposes moving west, the east one proposes moving east, and the middle one proposes moving north; all three succeed in moving:

..#..
....#
#....
....#
.....
..#..
At this point, no Elves need to move, and so the process ends.

The larger example above proceeds as follows:

== Initial State ==
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............

== End of Round 1 ==
..............
.......#......
.....#...#....
...#..#.#.....
.......#..#...
....#.#.##....
..#..#.#......
..#.#.#.##....
..............
....#..#......
..............
..............

== End of Round 2 ==
..............
.......#......
....#.....#...
...#..#.#.....
.......#...#..
...#..#.#.....
.#...#.#.#....
..............
..#.#.#.##....
....#..#......
..............
..............

== End of Round 3 ==
..............
.......#......
.....#....#...
..#..#...#....
.......#...#..
...#..#.#.....
.#..#.....#...
.......##.....
..##.#....#...
...#..........
.......#......
..............

== End of Round 4 ==
..............
.......#......
......#....#..
..#...##......
...#.....#.#..
.........#....
.#...###..#...
..#......#....
....##....#...
....#.........
.......#......
..............

== End of Round 5 ==
.......#......
..............
..#..#.....#..
.........#....
......##...#..
.#.#.####.....
...........#..
....##..#.....
..#...........
..........#...
....#..#......
..............
After a few more rounds...

== End of Round 10 ==
.......#......
...........#..
..#.#..#......
......#.......
...#.....#..#.
.#......##....
.....##.......
..#........#..
....#.#..#....
..............
....#..#..#...
..............
To make sure they're on the right track, the Elves like to check after round 10 that they're making good progress toward covering enough ground. To do this, count the number of empty ground tiles contained by the smallest rectangle that contains every Elf. (The edges of the rectangle should be aligned to the N/S/E/W directions; the Elves do not have the patience to calculate arbitrary rectangles.) In the above example, that rectangle is:

......#.....
..........#.
.#.#..#.....
.....#......
..#.....#..#
#......##...
....##......
.#........#.
...#.#..#...
............
...#..#..#..
In this region, the number of empty ground tiles is 110.

Simulate the Elves' process and find the smallest rectangle that contains the Elves after 10 rounds. How many empty ground tiles does that rectangle contain?
"""

from collections import defaultdict
from enum import Enum


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3


Grid = dict[int, dict[int, str]]


def has_elf(grid: Grid, row, col) -> bool:
    if row in grid and col in grid[row]:
        return True
    return False


def get_bounds(grid: Grid) -> tuple[int, int, int, int]:
    min_row = 10000
    max_row = -1
    min_col = 10000
    max_col = -1
    for row in grid:
        if row > max_row:
            max_row = row
        if row < min_row:
            min_row = row
        for col in grid[row]:
            if col > max_col:
                max_col = col
            if col < min_col:
                min_col = col
    return (min_row, max_row, min_col, max_col)


def count_blank(grid) -> int:
    min_row, max_row, min_col, max_col = get_bounds(grid)
    blank_ct = 0
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if not has_elf(grid, row, col):
                blank_ct += 1
    return blank_ct


def print_grid(grid: Grid):
    min_row, max_row, min_col, max_col = get_bounds(grid)
    for row in range(min_row, max_row + 1):
        grid_row = ""
        for col in range(min_col, max_col + 1):
            if not has_elf(grid, row, col):
                grid_row += "."
            else:
                grid_row += "#"
        print(grid_row)


def propose_moves(grid: Grid, start_dir: Direction) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    proposed_moves = []
    for row in grid:
        for col in grid[row]:
            if (
                not has_elf(grid, row - 1, col - 1)
                and not has_elf(grid, row - 1, col)
                and not has_elf(grid, row - 1, col + 1)
                and not has_elf(grid, row, col - 1)
                and not has_elf(grid, row, col + 1)
                and not has_elf(grid, row + 1, col - 1)
                and not has_elf(grid, row + 1, col)
                and not has_elf(grid, row + 1, col + 1)
            ):
                proposed_dest = (row, col)
            else:
                proposed_dest = (row, col)
                for i in range(4):
                    d = Direction((start_dir.value + i) % 4)
                    # print(row, col, d)
                    if d == Direction.NORTH:
                        if (
                            not has_elf(grid, row - 1, col - 1)
                            and not has_elf(grid, row - 1, col)
                            and not has_elf(grid, row - 1, col + 1)
                        ):
                            proposed_dest = (row - 1, col)
                            break
                    elif d == Direction.SOUTH:
                        if (
                            not has_elf(grid, row + 1, col - 1)
                            and not has_elf(grid, row + 1, col)
                            and not has_elf(grid, row + 1, col + 1)
                        ):
                            proposed_dest = (row + 1, col)
                            break
                    elif d == Direction.EAST:
                        if (
                            not has_elf(grid, row - 1, col + 1)
                            and not has_elf(grid, row, col + 1)
                            and not has_elf(grid, row + 1, col + 1)
                        ):
                            proposed_dest = (row, col + 1)
                            break
                    elif d == Direction.WEST:
                        if (
                            not has_elf(grid, row - 1, col - 1)
                            and not has_elf(grid, row, col - 1)
                            and not has_elf(grid, row + 1, col - 1)
                        ):
                            proposed_dest = (row, col - 1)
                            break
            move = ((row, col), proposed_dest)
            proposed_moves.append(move)
    return proposed_moves


def make_moves(proposed_moves) -> tuple[Grid, bool]:
    new_grid = {}
    move_cts = defaultdict(int)
    changed = False
    for _, move_loc in proposed_moves:
        move_cts[move_loc] += 1
    for curr_loc, move_loc in proposed_moves:
        ct = move_cts[move_loc]
        if ct == 1:
            if curr_loc != move_loc:
                changed = True
            row, col = move_loc
        else:
            row, col = curr_loc
        if row not in new_grid:
            new_grid[row] = {}
        new_grid[row][col] = "#"

    return new_grid, changed


def run_round(grid: Grid, d: Direction) -> tuple[Grid, bool]:
    # print("Start direction: ", d)
    proposed_moves = propose_moves(grid, d)
    new_grid, changed = make_moves(proposed_moves)
    return new_grid, changed


def run_rounds(grid: Grid, num_rounds: int) -> Grid:
    d = Direction.NORTH
    for _ in range(num_rounds):
        grid, changed = run_round(grid, d)
        if not changed:
            break
        d = Direction((d.value + 1) % 4)
        # print()
        # print_grid(grid)
        # print()
    return grid


def count_rounds(grid: Grid) -> int:
    d = Direction.NORTH
    ct = 0
    while True:
        ct += 1
        grid, changed = run_round(grid, d)
        if not changed:
            break
        d = Direction((d.value + 1) % 4)
        # print()
        # print_grid(grid)
        # print()
    return ct


def test_sample_large():
    input_lines = parse_input(SAMPLE_INPUT)
    grid = read_grid_lines(input_lines)
    new_grid = run_rounds(grid, 10)
    assert count_blank(new_grid) == 110
    ct = count_rounds(grid)
    assert ct == 20


def test_sample_small():
    input_lines = parse_input(SAMPLE_INPUT_SMALL)
    grid = read_grid_lines(input_lines)
    # run_rounds(grid, 10)
    ct = count_rounds(grid)
    assert ct == 4


def read_grid_lines(lines: list[str]) -> dict[int, dict[int, str]]:
    grid = {}
    for row, line in enumerate(lines):
        grid[row] = {}
        col = 0
        for col, c in enumerate(line):
            if c in ["#"]:
                grid[row][col] = c
    return grid


SAMPLE_INPUT_SMALL = """
.....
..##.
..#..
.....
..##.
.....
"""

SAMPLE_INPUT = """
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""


def parse_input(text: str) -> list[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    input_lines = parse_input(input_text)
    grid = read_grid_lines(input_lines)
    new_grid = run_rounds(grid, 10)
    print("Part 1:", count_blank(new_grid))
    print("part 2: ", count_rounds(grid))


if __name__ == "__main__":
    main()