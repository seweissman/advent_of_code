"""
--- Day 14: Regolith Reservoir ---
The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.

Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.
The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.
After a total of five units of sand have come to rest, they form this pattern:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.
After a total of 22 units of sand:

......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.
Finally, only two more units of sand can possibly come to rest:

......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.
Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........
Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?

"""

from collections import namedtuple
from enum import Enum
from typing import Dict, List, Tuple

Point = namedtuple("Point", ["col", "row"])

class Grid:
    def __init__(self):
        self.contents: Dict[Point, str] = {}
        self.max_row = -1
        self.max_col = -1
        self.min_col = -1

    def _update_min_max(self, row, col):
        if self.min_col == -1:
            self.min_col = col
        if self.max_col == -1:
            self.max_col = col
        if self.max_row == -1:
            self.max_row = row

        if col < self.min_col:
            self.min_col = col
        if col > self.max_col:
            self.max_col = col
        if row > self.max_row:
            self.max_row = row

    def add_rock_range(self, start: Point, end: Point):

        self._update_min_max(start.row, start.col)
        self._update_min_max(end.row, end.col)

        if start.row == end.row:
            # Horizontal
            min_col = min(start.col, end.col)
            max_col = max(start.col, end.col)
            for col in range(min_col, max_col + 1):
                self.contents[Point(col, start.row)] = "#"
        else:
            # Vertical
            min_row = min(start.row, end.row)
            max_row = max(start.row, end.row)
            for row in range(min_row, max_row + 1):
                self.contents[Point(start.col, row)] = "#"

    def add_sand(self, row: int, col: int):
        # Don't update max_row when we add sand
        self._update_min_max(self.max_row, col)
        self.contents[Point(col, row)] = "o"

    def occupied(self, row: int, col: int) -> bool:
        return Point(col, row) in self.contents

    def get_contents(self, row, col) -> str:
        return self.contents[Point(col, row)]

    def out_of_bounds(self, row: int, col: int) -> bool:
        if row > self.max_row:
            return True
        return False

    def print(self, min_col=None, max_col=None):
        if min_col is None:
            min_col = self.min_col
        if max_col is None:
            max_col = self.max_col
        print("\n")
        for row in range(0, self.max_row + 1):
            row_str = ""
            for col in range(min_col, max_col + 1):
                if self.occupied(row, col):
                    row_str += self.get_contents(row, col)
                else:
                    row_str += "."
            print(row_str)
        print("\n")

    @classmethod
    def build_grid(cls, input_lines) -> "Grid":
        def make_ranges(input_line: str) -> List[Tuple[Point, Point]]:
            ranges = []
            input_points = input_line.split(" -> ")
            range_pairs = [(input_points[i], input_points[i + 1]) for i in range(0, len(input_points) - 1)]
            for start_str, end_str in range_pairs:
                start = Point(*[int(s) for s in start_str.split(",")])
                end = Point(*[int(s) for s in end_str.split(",")])
                ranges.append((start, end))
            return ranges

        grid = cls()
        for line in input_lines:
            ranges = make_ranges(line)
            for r in ranges:
                grid.add_rock_range(*r)
        return grid


class InfiniteFloorGrid(Grid):
    def occupied(self, row: int, col: int) -> bool:
        if row >= self.max_row + 2:
            return True
        return super().occupied(row, col)

    def out_of_bounds(self, row: int, col: int) -> bool:
        return False


def drop_sand(grid: Grid) -> bool:
    """
    Returns true if sand comes to rest, False if it falls off grid or there is no more room in the grid.
    """
    curr_row = 0
    curr_col = 500
    if grid.occupied(curr_row, curr_col):
        return False
    while True:
        if not grid.occupied(curr_row + 1, curr_col):
            curr_row += 1
        elif not grid.occupied(curr_row + 1, curr_col - 1):
            curr_row += 1
            curr_col -= 1
        elif not grid.occupied(curr_row + 1, curr_col + 1):
            curr_row += 1
            curr_col += 1
        else:
            break

        if grid.out_of_bounds(curr_row, curr_col):
            return False

    grid.add_sand(curr_row, curr_col)
    return True


def test_sample_grid():
    input_lines = parse_input(SAMPLE_INPUT)
    grid = Grid.build_grid(input_lines)
    sand_count = 0
    while drop_sand(grid):
        sand_count += 1
    grid.print()
    assert sand_count == 24

    grid = InfiniteFloorGrid.build_grid(input_lines)
    sand_count = 0
    while drop_sand(grid):
        sand_count += 1
    grid.print()
    assert sand_count == 93


SAMPLE_INPUT = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def parse_input(text: str) -> List:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    lines = parse_input(input_text)
    grid = Grid.build_grid(lines)
    sand_count = 0
    while drop_sand(grid):
        sand_count += 1
    print("Part 1: ", sand_count)
    grid.print()

    grid = InfiniteFloorGrid.build_grid(lines)
    sand_count = 0
    while drop_sand(grid):
        sand_count += 1
    print("Part 2: ", sand_count)
    grid.print(min_col=450, max_col=550)


if __name__ == "__main__":
    main()