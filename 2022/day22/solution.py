"""
"""

from enum import Enum


class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


def turn(current_direction: Direction, letter: str) -> Direction:
    if letter == "L":
        current_direction.value
        return Direction((current_direction.value - 1) % 4)
    return Direction((current_direction.value + 1) % 4)


def test_turn():
    d = Direction.NORTH
    assert turn(d, "L") == Direction.WEST
    d = Direction.SOUTH
    assert turn(d, "R") == Direction.WEST
    d = Direction.EAST
    assert turn(d, "R") == Direction.SOUTH


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

    def __init__(self, grid, path: str):
        self.row = 0
        self.direction = Direction.NORTH
        self.path = path
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
        # self.run_index = self.run_index % len(self.grid[self.row])
        return self.run_index

    def set_run_index(self, v: int):
        self.run_index = v % len(self.grid[self.row])

    def get_col(self):
        # last_run = self.grid[self.row][-1]
        # row_width = last_run[1] + last_run[2]
        # self.col = self.col % row_width
        return self.col

    def set_col(self, v: int):
        first_run = self.grid[self.row][0]
        last_run = self.grid[self.row][-1]
        row_min = first_run[1]
        row_max = last_run[1] + last_run[2] - 1
        self.col = (v - row_min) % (row_max - row_min + 1) + row_min

    def get_row(self):
        # col_min = self._get_col_min()
        # col_max = self._get_col_max()
        # self.row = (self.row - col_min) % (col_max + 1 - col_min) + col_min
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


def walk_grid(grid: Grid, path):
    direction = Direction.NORTH
    while path:
        turn_letter, steps, path = next_direction(path)
        direction = turn(direction, turn_letter)
        print(direction, turn_letter, steps, grid.row, grid.col)
        # if grid.row == 1 and grid.col == 99:
        #     import pdb

        #     pdb.set_trace()
        if direction == Direction.SOUTH:
            grid.walk_down(steps)
        elif direction == Direction.NORTH:
            grid.walk_up(steps)
        elif direction == Direction.EAST:
            grid.walk_right(steps)
        else:
            grid.walk_left(steps)
    return direction


def test_walk_grid():
    input_lines = parse_input(SAMPLE_INPUT)
    grid_lines = input_lines[0 : len(input_lines) - 1]
    path = "R" + input_lines[-1]
    print(grid_lines)
    grid_rows = read_grid(grid_lines)
    grid = Grid(grid_rows, path)
    dir = walk_grid(grid, path)
    score = 1000 * (grid.row + 1) + 4 * (grid.col + 1) + dir.value
    assert score == 6032


def read_grid(lines: list[str]) -> list[list[tuple[str, int, int]]]:
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
    input_lines = parse_input(SAMPLE_INPUT)
    grid_lines = input_lines[0 : len(input_lines) - 1]
    path = "R3R3R12L1R20L7"
    print(grid_lines)
    grid_rows = read_grid(grid_lines)
    grid = Grid(grid_rows, path)
    dir = walk_grid(grid, path)
    print(grid.row, grid.col)


def test_read_grid():
    input_lines = parse_input(SAMPLE_INPUT)
    grid_lines = input_lines[0 : len(input_lines) - 1]
    grid = read_grid(grid_lines)
    assert grid[0] == [(".", 8, 3), ("#", 11, 1)]


def parse_input(text: str) -> list[str]:
    """Parse lines of input from raw text"""
    lines = [line for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    input_lines = parse_input(input_text)
    grid_lines = input_lines[0 : len(input_lines) - 1]
    path = "R" + input_lines[-1]
    grid_rows = read_grid(grid_lines)
    grid = Grid(grid_rows, path)
    dir = walk_grid(grid, path)
    score = 1000 * (grid.row + 1) + 4 * (grid.col + 1) + dir.value
    print("Part 1:", score)


if __name__ == "__main__":
    main()