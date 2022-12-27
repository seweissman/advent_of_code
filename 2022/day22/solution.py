"""
--- Day 22: Monkey Map ---
The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly the right direction according to your handheld device's Grove Positioning System.

As you walk, the monkeys explain that the grove is protected by a force field. To pass through the force field, you have to enter a password; doing so involves tracing a specific path on a strangely-shaped board.

At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.

The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

For example:

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
The first half of the monkeys' notes is a map of the board. It is comprised of a set of open tiles (on which you can move, drawn .) and solid walls (tiles which you cannot enter, drawn #).

The second half is a description of the path you must follow. It consists of alternating numbers and letters:

A number indicates the number of tiles to move in the direction you are facing. If you run into a wall, you stop moving forward and continue with the next instruction.
A letter indicates whether to turn 90 degrees clockwise (R) or counterclockwise (L). Turning happens in-place; it does not change your current tile.
So, a path like 10R5 means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".

You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right (from the perspective of how the map is drawn).

If a movement instruction would take you off of the map, you wrap around to the other side of the board. In other words, if your next tile is off of the board, you should instead look in the direction opposite of your current facing as far as you can until you find the opposite edge of the board, then reappear there.

For example, if you are at A and facing to the right, the tile in front of you is marked B; if you are at C and facing down, the tile in front of you is marked D:

        ...#
        .#..
        #...
        ....
...#.D.....#
........#...
B.#....#...A
.....C....#.
        ...#....
        .....#..
        .#......
        ......#.
It is possible for the next tile (after wrapping around) to be a wall; this still counts as there being a wall in front of you, and so movement stops before you actually wrap to the other side of the board.

By drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example looks like this:

        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#...v..v#    
>>>v...>#.>>    
..#v...#....    
...>>>>v..#.    
        ...#....
        .....#..
        .#......
        ......#.
To finish providing the password to this strange input device, you need to determine numbers for your final row, column, and facing as your final position appears from the perspective of the original map. Rows start from 1 at the top and count downward; columns start from 1 at the left and count rightward. (In the above example, row 1, column 1 refers to the empty space with no tile on it in the top-left corner.) Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). The final password is the sum of 1000 times the row, 4 times the column, and the facing.

In the above example, the final row is 6, the final column is 8, and the final facing is 0. So, the final password is 1000 * 6 + 4 * 8 + 0: 6032.

Follow the path given in the monkeys' notes. What is the final password?

Your puzzle answer was 159034.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?

You approach the strange input device, but it isn't quite what the monkeys drew in their notes. Instead, you are met with a large cube; each of its six faces is a square of 50x50 tiles.

To be fair, the monkeys' map does have six 50x50 regions on it. If you were to carefully fold the map, you should be able to shape it into a cube!

In the example above, the six (smaller, 4x4) faces of the cube are:

        1111
        1111
        1111
        1111
222233334444
222233334444
222233334444
222233334444
        55556666
        55556666
        55556666
        55556666
You still start in the same position and with the same facing as before, but the wrapping rules are different. Now, if you would walk off the board, you instead proceed around the cube. From the perspective of the map, this can look a little strange. In the above example, if you are at A and move to the right, you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:

        ...#
        .#..
        #...
        ....
...#.......#
........#..A
..#....#....
.D........#.
        ...#..B.
        .....#..
        .#......
        ..C...#.
Walls still block your path, even if they are on a different face of the cube. If you are at E facing up, your movement is blocked by the wall marked by the arrow:

        ...#
        .#..
     -->#...
        ....
...#..E....#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.
Using the same method of drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example now looks like this:

        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#..^...v#    
.>>>>>^.#.>>    
.^#....#....    
.^........#.    
        ...#..v.
        .....#v.
        .#v<<<<.
        ..v...#.
The final password is still calculated from your final position and facing from the perspective of the map. In this example, the final row is 5, the final column is 7, and the final facing is 3, so the final password is 1000 * 5 + 4 * 7 + 3 = 5031.

Fold the map into a cube, then follow the path given in the monkeys' notes. What is the final password?
"""

from collections import defaultdict, namedtuple
from enum import Enum


class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


QuadrantDirections = namedtuple("QuadrantDirections", ["north_to", "south_to", "west_to", "east_to"])

DIR_MAP: dict[int, QuadrantDirections] = {}
# 1
qd1 = QuadrantDirections(
    north_to=(2, Direction.SOUTH),
    west_to=(3, Direction.SOUTH),
    east_to=(6, Direction.WEST),
    south_to=(4, Direction.SOUTH),
)
# 2
qd2 = QuadrantDirections(
    north_to=(1, Direction.SOUTH),
    south_to=(5, Direction.NORTH),
    east_to=(3, Direction.EAST),
    west_to=(6, Direction.NORTH),
)
# 3
qd3 = QuadrantDirections(
    north_to=(1, Direction.EAST),
    south_to=(5, Direction.EAST),
    east_to=(4, Direction.EAST),
    west_to=(2, Direction.WEST),
)
# 4
qd4 = QuadrantDirections(
    north_to=(1, Direction.NORTH),
    south_to=(5, Direction.SOUTH),
    east_to=(6, Direction.SOUTH),
    west_to=(3, Direction.WEST),
)
# 5
qd5 = QuadrantDirections(
    north_to=(4, Direction.NORTH),
    south_to=(2, Direction.NORTH),
    east_to=(6, Direction.EAST),
    west_to=(3, Direction.NORTH),
)
# 6
qd6 = QuadrantDirections(
    north_to=(4, Direction.WEST),
    south_to=(2, Direction.EAST),
    east_to=(1, Direction.WEST),
    west_to=(5, Direction.WEST),
)

DIR_MAP[1] = qd1
DIR_MAP[2] = qd2
DIR_MAP[3] = qd3
DIR_MAP[4] = qd4
DIR_MAP[5] = qd5
DIR_MAP[6] = qd6

def test_turn():
    grid, _ = read_grid(SAMPLE_INPUT)
    assert grid.direction == Direction.NORTH
    grid.turn("L")
    assert grid.direction == Direction.WEST
    grid.direction = Direction.SOUTH
    grid.turn("R")
    assert grid.direction == Direction.WEST
    grid.direction = Direction.EAST
    grid.turn("R")
    assert grid.direction == Direction.SOUTH


def next_direction(path_str: str):
    dir_str = path_str[0]
    steps_str = ""
    i = 0
    for i, c in enumerate(path_str[1:]):
        if c not in ["L", "R"]:
            steps_str += c
        else:
            break
    steps = int(steps_str)
    remaining_path_str = path_str[i + 1 :]
    if len(remaining_path_str) == 1:
        remaining_path_str = ""
    return dir_str, steps, remaining_path_str


def test_next_direction():
    path = "R10R5L5R10L4R5L5"
    dir_str, steps, path = next_direction(path)
    assert dir_str == "R"
    assert steps == 10
    assert path == "R5L5R10L4R5L5"
    dir_str, steps, path = next_direction(path)
    assert dir_str == "R"
    assert steps == 5


class Grid:

    def __init__(self, grid: dict[int, dict[int, str]]):
        self.row = 0
        self.direction = Direction.NORTH
        self.col = 0
        self.row_grid = grid
        self.col_grid: dict[int, dict[int, str]] = {}
        for row, col_dict in self.row_grid.items():
            for col, val in col_dict.items():
                if col not in self.col_grid:
                    self.col_grid[col] = {}
                self.col_grid[col][row] = val

        self.col_min = {}
        self.col_max = {}
        self.col_bounds = {}
        self.col = min(self.row_grid[0].keys())

    def _get_col_min(self):
        return min(self.row_grid[self.row].keys())

    def _get_col_max(self):
        return max(self.row_grid[self.row].keys())

    def _get_row_min(self):
        return min(self.col_grid[self.col].keys())

    def _get_row_max(self):
        return max(self.col_grid[self.col].keys())

    def get_col(self):
        return self.col

    def step_row(self, backwards=False):
        direction = self.direction
        if backwards:
            direction = Direction((self.direction.value + 2) % 4)

        if direction == Direction.SOUTH:
            v = self.row + 1
        else:
            v = self.row - 1
        row_min = self._get_row_min()
        row_max = self._get_row_max()
        self.row = (v - row_min) % (row_max - row_min + 1) + row_min

    def get_row(self):
        return self.row

    def step_col(self, backwards=False):
        direction = self.direction
        if backwards:
            direction = Direction((self.direction.value + 2) % 4)

        if direction == Direction.EAST:
            v = self.col + 1
        else:
            v = self.col - 1
        col_min = self._get_col_min()
        col_max = self._get_col_max()
        self.col = (v - col_min) % (col_max - col_min + 1) + col_min

    def turn(self, letter: str):
        if letter == "L":
            self.direction = Direction((self.direction.value - 1) % 4)
        else:
            self.direction = Direction((self.direction.value + 1) % 4)

    def walk(self, letter: str, steps: int):
        self.turn(letter)
        print(self.direction, letter, steps, self.row, self.col)
        # if self.row == 5 and self.col == 6:
        #     import pdb

        #     pdb.set_trace()
        while steps > 0:
            if self.direction in [Direction.EAST, Direction.WEST]:
                self.step_col()
            else:
                self.step_row()
            if self.row_grid[self.row][self.col] == "#":
                if self.direction in [Direction.EAST, Direction.WEST]:
                    self.step_col(backwards=True)
                else:
                    self.step_row(backwards=True)
                break
            steps -= 1

class Cube(Grid):
    def __init__(self, grid, size):
        super().__init__(grid)
        self.quadrant = 1
        self.size = size

    def move_quadrant(self, direction: Direction, backwards=False):
        q_dirs = DIR_MAP[self.quadrant]
        if direction == Direction.EAST:
            new_quadrant, new_direction = q_dirs.east_to
        elif direction == Direction.WEST:
            new_quadrant, new_direction = q_dirs.west_to
        elif direction == Direction.NORTH:
            new_quadrant, new_direction = q_dirs.north_to
        else:
            new_quadrant, new_direction = q_dirs.south_to

        if not backwards:
            self.direction = new_direction
        else:
            self.direction = Direction((new_direction.value + 2) % 4)

        if self.quadrant == 1:
            if new_quadrant == 2:
                self.row = self.size
                self.col = self.col - 2 * self.size
            if new_quadrant == 3:
                self.col = self.size + self.row
                self.row = self.size
            if new_quadrant == 4:
                self.row = self.size
                # self.col stays the same
            if new_quadrant == 6:
                self.row = 3 * self.size - self.row - 1
                self.col = 4 * self.size - 1
        elif self.quadrant == 2:
            if new_quadrant == 1:
                self.row = 0
                self.col = 3 * self.size - self.col - 1
            if new_quadrant == 3:
                self.col = self.size
                # self.row stays the same
            if new_quadrant == 5:
                self.row = 3 * self.size - 1
                self.col = 3 * self.size - self.col - 1
            if new_quadrant == 6:
                self.col = 3 * self.size - self.row - 1
                self.row = 3 * self.size
        elif self.quadrant == 3:
            if new_quadrant == 2:
                # self.row stays the same
                self.col = self.size - 1
            if new_quadrant == 4:
                # self.row stays the same
                self.col = 2 * self.size
            if new_quadrant == 1:
                self.row = self.col - self.size
                self.col = 2 * self.size
            if new_quadrant == 5:
                self.row = 3 * self.size - self.row - 1
                self.col = 2 * self.size
        elif self.quadrant == 4:
            if new_quadrant == 1:
                self.row = self.size - 1
                # self.col stays the same
            if new_quadrant == 3:
                self.col = 2 * self.size - 1
                # self.row stays the same
            if new_quadrant == 5:
                self.row = 2 * self.size
                # self.col stays the same
            if new_quadrant == 6:
                self.col = 5 * self.size - self.row - 1
                self.row = 2 * self.size
        elif self.quadrant == 5:
            if new_quadrant == 4:
                self.row = 2 * self.size - 1
                # self.col stays the same
            if new_quadrant == 6:
                self.col = 3 * self.size
                # self.row stays the same
            if new_quadrant == 3:
                self.col = 4 * self.size - self.row - 1
                self.row = 2 * self.size
            if new_quadrant == 2:
                self.row = 2 * self.size - 1
                self.col = 3 * self.size - self.col - 1
        else:  # if self.quadrant == 6:
            if new_quadrant == 5:
                # self.row stays the same
                self.col = 3 * self.size - 1
            if new_quadrant == 4:
                self.row = 4 * self.size - self.col - 1
                self.col = 3 * self.size - 1
            if new_quadrant == 1:
                self.row = 3 * self.size - self.row - 1
                self.col = 3 * self.size - 1
            if new_quadrant == 2:
                self.row = 3 * self.size - self.col - 1
                self.col = 0
        self.quadrant = new_quadrant

    def _get_col_min(self):
        if self.quadrant == 1:
            return 2 * self.size
        if self.quadrant == 2:
            return 0
        if self.quadrant == 3:
            return self.size
        if self.quadrant == 4:
            return 2 * self.size
        if self.quadrant == 5:
            return 2 * self.size
        # if self.quadrant == 6:
        return 3 * self.size

    def _get_col_max(self):
        if self.quadrant == 1:
            return 3 * self.size - 1
        if self.quadrant == 2:
            return self.size - 1
        if self.quadrant == 3:
            return 2 * self.size - 1
        if self.quadrant == 4:
            return 3 * self.size - 1
        if self.quadrant == 5:
            return 3 * self.size - 1
        # if self.quadrant == 6:
        return 4 * self.size - 1

    def _get_row_min(self):
        if self.quadrant == 1:
            return 0
        if self.quadrant == 2:
            return self.size
        if self.quadrant == 3:
            return self.size
        if self.quadrant == 4:
            return self.size
        if self.quadrant == 5:
            return 2 * self.size
        # if self.quadrant == 6:
        return 2 * self.size

    def _get_row_max(self):
        if self.quadrant == 1:
            return self.size - 1
        if self.quadrant == 2:
            return 2 * self.size - 1
        if self.quadrant == 3:
            return 2 * self.size - 1
        if self.quadrant == 4:
            return 2 * self.size - 1
        if self.quadrant == 5:
            return 3 * self.size - 1
        # if self.quadrant == 6:
        return 3 * self.size - 1

    def step_col(self, backwards=False):
        col_min = self._get_col_min()
        col_max = self._get_col_max()
        direction = self.direction
        if backwards:
            direction = Direction((self.direction.value + 2) % 4)

        if direction == Direction.WEST:
            if self.col == col_min:
                self.move_quadrant(Direction.WEST, backwards=backwards)
            else:
                self.col -= 1
        elif direction == Direction.EAST:
            if self.col == col_max:
                self.move_quadrant(Direction.EAST, backwards=backwards)
            else:
                self.col += 1

    def step_row(self, backwards=False):
        row_min = self._get_row_min()
        row_max = self._get_row_max()

        direction = self.direction
        if backwards:
            direction = Direction((self.direction.value + 2) % 4)

        if direction == Direction.NORTH:
            if self.row == row_min:
                self.move_quadrant(Direction.NORTH)
            else:
                self.row -= 1
        elif direction == Direction.SOUTH:
            if self.row == row_max:
                self.move_quadrant(Direction.SOUTH)
            else:
                self.row += 1


def walk_grid(grid: Grid, path):
    while path:
        turn_letter, steps, path = next_direction(path)
        print(turn_letter, steps, path)
        grid.walk(turn_letter, steps)


def test_walk_grid_part1():
    grid, path = read_grid(SAMPLE_INPUT)
    walk_grid(grid, path)
    score = 1000 * (grid.row + 1) + 4 * (grid.col + 1) + grid.direction.value
    assert score == 6032


def test_walk_grid_part2():
    cube, path = read_cube(SAMPLE_INPUT)
    walk_grid(cube, path)
    print("Last facing:", cube.direction)
    score = 1000 * (cube.row + 1) + 4 * (cube.col + 1) + cube.direction.value
    assert score == 5031


def read_grid_lines(lines: list[str]) -> dict[int, dict[int, str]]:
    grid = {}
    for row, line in enumerate(lines):
        grid[row] = {}
        col = 0
        for col, c in enumerate(line):
            if c in [".", "#"]:
                grid[row][col] = c
    return grid


def read_grid(input_str: str) -> tuple[Grid, str]:
    input_lines = parse_input(input_str)
    lines = input_lines[0 : len(input_lines) - 1]
    path = "R" + input_lines[-1]
    grid_dict = read_grid_lines(lines)
    grid = Grid(grid_dict)
    return grid, path


def read_cube(input_str: str, size=4) -> tuple[Cube, str]:
    input_lines = parse_input(input_str)
    lines = input_lines[0 : len(input_lines) - 1]
    path = "R" + input_lines[-1]
    grid_rows = read_grid_lines(lines)
    grid = Cube(grid_rows, size)
    return grid, path


SAMPLE_INPUT = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.
10R5L5R10L4R5L5
"""


def test_walk_grid2():
    path = "R3R3R12L1R20L7"
    grid, _ = read_grid(SAMPLE_INPUT)
    walk_grid(grid, path)
    assert grid.row == 7
    assert grid.col == 4


# def test_read_grid_lines():
#     input_lines = parse_input(SAMPLE_INPUT)
#     grid_lines = input_lines[0 : len(input_lines) - 1]
#     grid = read_grid_lines(grid_lines)
#     assert grid[0] == [(".", 8, 3), ("#", 11, 1)]


def parse_input(text: str) -> list[str]:
    """Parse lines of input from raw text"""
    lines = [line for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    # grid, path = read_grid(input_text)
    # walk_grid(grid, path)
    # score = 1000 * (grid.row + 1) + 4 * (grid.col + 1) + grid.direction.value
    # print("Part 1:", score)

    # part 2
    cube, path = read_cube(input_text)
    walk_grid(cube, path)
    score = 1000 * (cube.row + 1) + 4 * (cube.col + 1) + cube.direction.value
    print("Part 2:", score)


if __name__ == "__main__":
    main()