"""
--- Day 24: Blizzard Basin ---
With everything replanted for next year (and with elephants and monkeys to tend the grove), you and the Elves leave for the extraction point.

Partway up the mountain that shields the grove is a flat, open area that serves as the extraction point. It's a bit of a climb, but nothing the expedition can't handle.

At least, that would normally be true; now that the mountain is covered in snow, things have become more difficult than the Elves are used to.

As the expedition reaches a valley that must be traversed to reach the extraction site, you find that strong, turbulent winds are pushing small blizzards of snow and sharp ice around the valley. It's a good thing everyone packed warm clothes! To make it across safely, you'll need to find a way to avoid them.

Fortunately, it's easy to see all of this from the entrance to the valley, so you make a map of the valley and the blizzards (your puzzle input). For example:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#
The walls of the valley are drawn as #; everything else is ground. Clear ground - where there is currently no blizzard - is drawn as .. Otherwise, blizzards are drawn with an arrow indicating their direction of motion: up (^), down (v), left (<), or right (>).

The above map includes two blizzards, one moving right (>) and one moving down (v). In one minute, each blizzard moves one position in the direction it is pointing:

#.#####
#.....#
#.>...#
#.....#
#.....#
#...v.#
#####.#
Due to conservation of blizzard energy, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley moving in the same direction. After another minute, the bottom downward-moving blizzard has been replaced with a new downward-moving blizzard at the top of the valley instead:

#.#####
#...v.#
#..>..#
#.....#
#.....#
#.....#
#####.#
Because blizzards are made of tiny snowflakes, they pass right through each other. After another minute, both blizzards temporarily occupy the same position, marked 2:

#.#####
#.....#
#...2.#
#.....#
#.....#
#.....#
#####.#
After another minute, the situation resolves itself, giving each blizzard back its personal space:

#.#####
#.....#
#....>#
#...v.#
#.....#
#.....#
#####.#
Finally, after yet another minute, the rightward-facing blizzard on the right is replaced with a new one on the left facing the same direction:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#
This process repeats at least as long as you are observing it, but probably forever.

Here is a more complex example:

#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
Your expedition begins in the only non-wall position in the top row and needs to reach the only non-wall position in the bottom row. On each minute, you can move up, down, left, or right, or you can wait in place. You and the blizzards act simultaneously, and you cannot share a position with a blizzard.

In the above example, the fastest way to reach your goal requires 18 steps. Drawing the position of the expedition as E, one way to achieve this is:

Initial state:
#E######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Minute 1, move down:
#.######
#E>3.<.#
#<..<<.#
#>2.22.#
#>v..^<#
######.#

Minute 2, move down:
#.######
#.2>2..#
#E^22^<#
#.>2.^>#
#.>..<.#
######.#

Minute 3, wait:
#.######
#<^<22.#
#E2<.2.#
#><2>..#
#..><..#
######.#

Minute 4, move up:
#.######
#E<..22#
#<<.<..#
#<2.>>.#
#.^22^.#
######.#

Minute 5, move right:
#.######
#2Ev.<>#
#<.<..<#
#.^>^22#
#.2..2.#
######.#

Minute 6, move right:
#.######
#>2E<.<#
#.2v^2<#
#>..>2>#
#<....>#
######.#

Minute 7, move down:
#.######
#.22^2.#
#<vE<2.#
#>>v<>.#
#>....<#
######.#

Minute 8, move left:
#.######
#.<>2^.#
#.E<<.<#
#.22..>#
#.2v^2.#
######.#

Minute 9, move up:
#.######
#<E2>>.#
#.<<.<.#
#>2>2^.#
#.v><^.#
######.#

Minute 10, move right:
#.######
#.2E.>2#
#<2v2^.#
#<>.>2.#
#..<>..#
######.#

Minute 11, wait:
#.######
#2^E^2>#
#<v<.^<#
#..2.>2#
#.<..>.#
######.#

Minute 12, move down:
#.######
#>>.<^<#
#.<E.<<#
#>v.><>#
#<^v^^>#
######.#

Minute 13, move down:
#.######
#.>3.<.#
#<..<<.#
#>2E22.#
#>v..^<#
######.#

Minute 14, move right:
#.######
#.2>2..#
#.^22^<#
#.>2E^>#
#.>..<.#
######.#

Minute 15, move right:
#.######
#<^<22.#
#.2<.2.#
#><2>E.#
#..><..#
######.#

Minute 16, move right:
#.######
#.<..22#
#<<.<..#
#<2.>>E#
#.^22^.#
######.#

Minute 17, move down:
#.######
#2.v.<>#
#<.<..<#
#.^>^22#
#.2..2E#
######.#

Minute 18, move down:
#.######
#>2.<.<#
#.2v^2<#
#>..>2>#
#<....>#
######E#
What is the fewest number of minutes required to avoid the blizzards and reach the goal?
"""

from collections import defaultdict
from enum import Enum


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3


class Blizzard:
    def __init__(self, row, col, direction, limit):
        self.row = row
        self.col = col
        self.direction = direction
        self.limit = limit

    def move(self):
        if self.direction == Direction.NORTH:
            self.row = (self.row - 1) % self.limit
        elif self.direction == Direction.SOUTH:
            self.row = (self.row + 1) % self.limit
        elif self.direction == Direction.EAST:
            self.col = (self.col + 1) % self.limit
        else:  # self.direction == Direction.WEST:
            self.col = (self.col - 1) % self.limit

    def get_state(self):
        return self.row, self.col, self.direction, self.limit


def search_path(
    blizzards: list[Blizzard],
    end: tuple[int, int],
    row_limit: int,
    col_limit,
    repeat_time=12,
):
    minute = 0
    start_row = -1
    start_col = 0
    start = (start_row, start_col)
    min_dist = 100000
    # print("END: ", end, row_limit, col_limit)
    end_row, end_col = end
    seen = set()
    min_time_to_point = dict()

    curr_states = [(minute, start, {(0, start)})]
    while True:
        new_states = []
        for blizzard in blizzards:
            blizzard.move()

        blizzard_locs = set()
        for blizzard in blizzards:
            blizzard_locs.add((blizzard.row, blizzard.col))

        for state in curr_states:
            minute, position, seen_points = state
            row, col = position

            if position not in min_time_to_point:
                min_time_to_point[position] = minute

            # dist = end_row - row + end_col - col
            # if dist < min_dist:
            #     min_dist = dist
            #     print(min_dist, minute, len(curr_states))
            if position == end:
                return minute, seen_points
            if (minute % repeat_time, position) in seen:
                continue
            seen.add((minute % repeat_time, position))
            possible_moves = [(row, col), (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for move in possible_moves:
                move_row, move_col = move
                if (0 <= move_row < row_limit and 0 <= move_col < col_limit) or move == end:
                    if move not in blizzard_locs:

                        if (
                            move in min_time_to_point
                            and move not in seen_points
                            and minute + 1 > min_time_to_point[move] + 10
                        ):
                            continue

                        new_seen_points = seen_points.copy()
                        new_seen_points.add(move)
                        new_states.append((minute + 1, move, new_seen_points))
        curr_states = new_states


def search_path_part2(
    blizzards: list[Blizzard],
    end: tuple[int, int],
    row_limit: int,
    col_limit,
    repeat_time=12,
):
    minute = 0
    start_row = -1
    start_col = 0
    start = (start_row, start_col)
    # min_dist = 100000
    # print("END: ", end, row_limit, col_limit)
    end_row, end_col = end
    seen = set()
    leg = 0
    min_time_to_point = dict()

    curr_states = [(minute, leg, start, {(0, start)})]
    while True:
        new_states = []
        for blizzard in blizzards:
            blizzard.move()

        blizzard_locs = set()
        for blizzard in blizzards:
            blizzard_locs.add((blizzard.row, blizzard.col))

        for state in curr_states:
            minute, leg, position, seen_points = state
            if leg > 2:
                continue
            row, col = position

            if position not in min_time_to_point:
                min_time_to_point[(leg, position)] = minute

            # if leg in [0, 2]:
            #     dist = end_row - row + end_col - col
            # else:
            #     dist = row - start[0] + col - start[1]
            # dist += (2 - leg) * (row_limit + col_limit)
            # if dist < min_dist:
            #     min_dist = dist
            #     print(min_dist, minute, len(curr_states))
            if position == end and leg == 2:
                return minute, seen_points
            if (minute % repeat_time, leg, position) in seen:
                continue
            seen.add((minute % repeat_time, leg, position))
            if position == start:
                possible_moves = [start, (0, 0)]
            elif position == end:
                possible_moves = [end, (row_limit - 1, col_limit - 1)]
            else:
                possible_moves = [(row, col), (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for move in possible_moves:
                move_row, move_col = move
                if (
                    (0 <= move_row < row_limit and 0 <= move_col < col_limit)
                    or (leg == 1 and move == start)
                    or (leg in [0, 2] and move == end)
                ):
                    if move not in blizzard_locs:
                        new_leg = leg
                        if new_leg in [0, 2] and position == end:
                            new_leg += 1
                        elif new_leg == 1 and position == start:
                            new_leg += 1

                        if (
                            (new_leg, move) in min_time_to_point
                            and (new_leg, move) not in seen_points
                            and minute + 1 > min_time_to_point[(new_leg, move)] + 10
                        ):
                            continue

                        new_seen_points = seen_points.copy()
                        new_seen_points.add((new_leg, move))
                        new_states.append((minute + 1, new_leg, move, new_seen_points))
        curr_states = new_states


def make_blizzards(lines) -> list[Blizzard]:
    blizzards = []
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            blizzard = None
            if c == ">":
                blizzard = Blizzard(row, col - 1, Direction.EAST, len(line) - 2)
            elif c == "^":
                blizzard = Blizzard(row, col - 1, Direction.NORTH, len(lines))
            elif c == "<":
                blizzard = Blizzard(row, col - 1, Direction.WEST, len(line) - 2)
            elif c == "v":
                blizzard = Blizzard(row, col - 1, Direction.SOUTH, len(lines))
            if blizzard:
                blizzards.append(blizzard)
    return blizzards


def print_grid(blizzards, row_limit, col_limit, expedition_point):
    exp_row, exp_col = expedition_point
    print("\n")
    if exp_row == -1:
        print("#E" + "#" * col_limit)
    else:
        print("#" * (col_limit + 2))
    blizzard_dict = defaultdict(list)
    for blizzard in blizzards:
        blizzard_dict[(blizzard.row, blizzard.col)].append(blizzard)

    for row in range(row_limit):
        row_str = "#"
        for col in range(col_limit):
            if (row, col) == expedition_point:
                row_str += "E"
                if (row, col) in blizzard_dict:
                    raise Exception(f"Blizzard at expedition point {expedition_point}")
            elif (row, col) in blizzard_dict:
                blizzard_list = blizzard_dict[(row, col)]
                if len(blizzard_list) > 1:
                    row_str += str(len(blizzard_list))
                else:
                    blizzard = blizzard_list[0]
                    if blizzard.direction == Direction.EAST:
                        row_str += ">"
                    elif blizzard.direction == Direction.WEST:
                        row_str += "<"
                    elif blizzard.direction == Direction.SOUTH:
                        row_str += "v"
                    elif blizzard.direction == Direction.NORTH:
                        row_str += "^"
            else:
                row_str += "."
        print(row_str + "#")

    if exp_row == row_limit:
        print("#" * col_limit + "E#")
    else:
        print("#" * (col_limit + 2))


def test_print_grid():
    input_lines = parse_input(SAMPLE_INPUT_COMPLEX)
    row_limit = len(input_lines) - 2
    col_limit = len(input_lines[0]) - 2
    blizzards = make_blizzards(input_lines[1:-1])

    print_grid(blizzards, row_limit, col_limit, (-1, 0))


SAMPLE_INPUT_SIMPLE = """#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#"""


def test_make_blizzards():
    input_lines = parse_input(SAMPLE_INPUT_SIMPLE)
    blizzards = make_blizzards(input_lines[1:-1])
    assert len(blizzards) == 2
    blizzard1 = blizzards[0]
    blizzard2 = blizzards[1]
    assert blizzard1.row == 1
    assert blizzard1.col == 0
    assert blizzard1.direction == Direction.EAST
    assert blizzard2.row == 3
    assert blizzard2.col == 3
    assert blizzard2.direction == Direction.SOUTH
    assert blizzard2.limit == 5
    assert blizzard1.limit == 5
    blizzard1.move()
    blizzard2.move()
    blizzard1.move()
    blizzard2.move()
    assert blizzard2.row == 0
    assert blizzard2.col == 3
    blizzard1.move()
    blizzard2.move()
    assert blizzard1.col == 3
    assert blizzard1.row == 1
    assert blizzard2.col == 3
    assert blizzard2.row == 1


SAMPLE_INPUT_COMPLEX = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""


def test_part1_complex():
    input_lines = parse_input(SAMPLE_INPUT_COMPLEX)
    print(input_lines[1:-1])
    blizzards = make_blizzards(input_lines[1:-1])
    row_limit = len(input_lines) - 2
    col_limit = len(input_lines[0]) - 2
    end = (len(input_lines) - 2, len(input_lines[0]) - 3)
    minute, path = search_path(blizzards, end, row_limit, col_limit)
    assert minute == 18


def test_part2_complex():
    input_lines = parse_input(SAMPLE_INPUT_COMPLEX)
    # print(input_lines[1:-1])
    blizzards = make_blizzards(input_lines[1:-1])
    row_limit = len(input_lines) - 2
    col_limit = len(input_lines[0]) - 2
    end = (len(input_lines) - 2, len(input_lines[0]) - 3)

    minute, path = search_path_part2(blizzards, end, row_limit, col_limit)
    assert minute == 54


def parse_input(text: str) -> list[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    input_lines = parse_input(input_text)
    # print(input_lines[1:-1])
    blizzards = make_blizzards(input_lines[1:-1])
    row_limit = len(input_lines) - 2
    col_limit = len(input_lines[0]) - 2
    end = (len(input_lines) - 2, len(input_lines[0]) - 3)

    minute, path = search_path(blizzards, end, row_limit, col_limit, repeat_time=300)
    print("Part 1:", minute)

    blizzards = make_blizzards(input_lines[1:-1])
    minute, path = search_path_part2(blizzards, end, row_limit, col_limit, repeat_time=300)
    print("Part 2:", minute)


if __name__ == "__main__":
    main()