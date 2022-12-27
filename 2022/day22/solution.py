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

from enum import Enum


class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


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

    def __init__(self, grid):
        self.row = 0
        self.direction = Direction.NORTH
        self.run_index = 0
        self.col = 0
        self.grid = grid
        self.col_min = {}
        self.col_max = {}
        self.col_bounds = {}
        self.col = self.grid[0][0][1]

    def _get_col_min(self):
        col = self.col  # get_col()
        if col in self.col_min:
            return self.col_min[col]
        row = 0
        while row < len(self.grid):
            for run in self.grid[row]:
                if run[0] in [".", "#"] and run[1] <= col < run[1] + run[2]:
                    return row
            row += 1
        self.col_min[col] = row
        return row

    def _get_col_max(self):
        col = self.get_col()
        if col in self.col_max:
            return self.col_max[col]
        row = len(self.grid) - 1
        while row > 0:
            for run in self.grid[row]:
                if run[0] in [".", "#"] and run[1] <= col < run[1] + run[2]:
                    return row
            row -= 1
        self.col_max[col] = row
        return row

    def get_run_index(self):
        return self.run_index

    def set_run_index(self, v: int):
        self.run_index = v % len(self.grid[self.row])

    def get_col(self):
        return self.col

    def set_col(self, v: int):
        first_run = self.grid[self.row][0]
        last_run = self.grid[self.row][-1]
        row_min = first_run[1]
        row_max = last_run[1] + last_run[2] - 1
        self.col = (v - row_min) % (row_max - row_min + 1) + row_min

    def get_row(self):
        return self.row

    def set_row(self, v: int):
        col_min = self._get_col_min()
        col_max = self._get_col_max()
        self.row = (v - col_min) % (col_max - col_min + 1) + col_min

    def _reset_run_index(self):
        self.run_index = 0
        while True:
            run = self.grid[self.get_row()][self.get_run_index()]
            if run[1] <= self.get_col() < run[1] + run[2]:
                break
            self.set_run_index(self.run_index + 1)

    def turn(self, letter: str):
        if letter == "L":
            self.direction = Direction((self.direction.value - 1) % 4)
        else:
            self.direction = Direction((self.direction.value + 1) % 4)

    def walk(self, letter: str, steps: int):
        self.turn(letter)
        print(self.direction, letter, steps, self.row, self.col)
        # if grid.row == 1 and grid.col == 99:
        #     import pdb

        #     pdb.set_trace()
        if self.direction == Direction.SOUTH:
            self.walk_down(steps)
        elif self.direction == Direction.NORTH:
            self.walk_up(steps)
        elif self.direction == Direction.EAST:
            self.walk_right(steps)
        else:
            self.walk_left(steps)

    def walk_right(self, steps: int):
        while steps > 0:
            run = self.grid[self.get_row()][self.get_run_index()]
            if run[0] == ".":
                steps_to_take = min(steps, run[2] - self.get_col() + run[1])
                self.set_col(self.col + steps_to_take)
                steps -= steps_to_take
            elif run[0] == "#":
                break
            self.set_run_index(self.get_run_index() + 1)
        run = self.grid[self.get_row()][self.get_run_index()]
        if run[0] == "#" and run[1] <= self.get_col() < run[1] + run[2]:
            self.set_run_index(self.get_run_index() - 1)
            self.set_col(self.col - 1)

    def walk_left(self, steps: int):
        while steps > 0:
            run = self.grid[self.get_row()][self.get_run_index()]
            if run[0] == ".":
                steps_to_take = min(steps, self.get_col() - run[1] + 1)
                steps = steps - steps_to_take
                self.set_col(self.get_col() - steps_to_take)
            elif run[0] == "#":
                break
            self.set_run_index(self.get_run_index() - 1)
        run = self.grid[self.get_row()][self.get_run_index()]
        if run[0] == "#" and run[1] <= self.get_col() < run[1] + run[2]:
            self.set_run_index(self.get_run_index() + 1)
            self.set_col(self.col + 1)

    def walk_down(self, steps: int):
        while steps > 0:
            self.set_row(self.get_row() + 1)
            self.run_index = 0
            while True:
                run = self.grid[self.get_row()][self.get_run_index()]
                if run[1] <= self.get_col() < run[1] + run[2]:
                    break
                self.set_run_index(self.run_index + 1)
            run = self.grid[self.get_row()][self.get_run_index()]
            if run[0] == ".":
                steps -= 1
            elif run[0] == "#":
                break
        run = self.grid[self.get_row()][self.get_run_index()]
        if run[0] == "#" and run[1] <= self.get_col() < run[1] + run[2]:
            self.set_row(self.get_row() - 1)
            self._reset_run_index()

    def walk_up(self, steps: int):
        while steps > 0:
            self.set_row(self.get_row() - 1)
            self.run_index = 0
            while True:
                run = self.grid[self.get_row()][self.get_run_index()]
                if run[1] <= self.get_col() < run[1] + run[2]:
                    break
                self.set_run_index(self.run_index + 1)
            run = self.grid[self.get_row()][self.get_run_index()]
            if run[0] == ".":
                steps -= 1
            elif run[0] == "#":
                break
        run = self.grid[self.get_row()][self.get_run_index()]
        if run[0] == "#" and run[1] <= self.get_col() < run[1] + run[2]:
            self.set_row(self.get_row() + 1)
            self._reset_run_index()


class Cube(Grid):
    def set_col(self, v: int):
        col_min = self._get_col_min()
        col_max = self._get_col_max()

    def set_row(self, v: int):
        first_run = self.grid[self.row][0]
        last_run = self.grid[self.row][-1]
        row_min = first_run[1]
        row_max = last_run[1] + last_run[2] - 1

    pass


def walk_grid(grid: Grid, path):
    while path:
        turn_letter, steps, path = next_direction(path)
        print(turn_letter, steps, path)
        grid.walk(turn_letter, steps)


def test_walk_grid():
    grid, path = read_grid(SAMPLE_INPUT)
    walk_grid(grid, path)
    score = 1000 * (grid.row + 1) + 4 * (grid.col + 1) + grid.direction.value
    assert score == 6032


def read_grid_lines(lines: list[str]) -> list[list[tuple[str, int, int]]]:
    grid = []
    for line in lines:
        grid_row = []
        curr_c = None
        c_ct = 0
        c_start = 0
        for c in line:
            if curr_c is None:
                curr_c = c
            if c == curr_c:
                c_ct += 1
            else:
                run = (curr_c, c_start, c_ct)
                if curr_c in [".", "#"]:
                    grid_row.append(run)
                c_start = c_start + c_ct
                c_ct = 0
                curr_c = c
                c_ct += 1
        run = (curr_c, c_start, c_ct)
        if curr_c in [".", "#"]:
            grid_row.append(run)
        grid.append(grid_row)
    return grid


def read_grid(input_str: str) -> tuple[Grid, str]:
    input_lines = parse_input(input_str)
    lines = input_lines[0 : len(input_lines) - 1]
    path = "R" + input_lines[-1]
    grid_rows = read_grid_lines(lines)
    grid = Grid(grid_rows)
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


def test_read_grid_lines():
    input_lines = parse_input(SAMPLE_INPUT)
    grid_lines = input_lines[0 : len(input_lines) - 1]
    grid = read_grid_lines(grid_lines)
    assert grid[0] == [(".", 8, 3), ("#", 11, 1)]


def parse_input(text: str) -> list[str]:
    """Parse lines of input from raw text"""
    lines = [line for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    grid = read_grid(input_text)
    walk_grid(grid)
    score = 1000 * (grid.row + 1) + 4 * (grid.col + 1) + grid.direction.value
    print("Part 1:", score)


if __name__ == "__main__":
    main()