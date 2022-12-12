"""
--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?

--- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
"""

import heapq
from collections import namedtuple
from typing import List

Point = namedtuple("Point", ["x", "y"])

SAMPLE_INPUT = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def next_points(curr_loc: Point, max_x: int, max_y: int) -> List[Point]:
    next_pts = []
    for x_diff in [-1, 1]:
        if 0 <= curr_loc.x + x_diff < max_x:
            next_pt = Point(curr_loc.x + x_diff, curr_loc.y)
            next_pts.append(next_pt)
    for y_diff in [-1, 1]:
        if 0 <= curr_loc.y + y_diff < max_y:
            next_pt = Point(curr_loc.x, curr_loc.y + y_diff)
            next_pts.append(next_pt)
    return next_pts


def test_next_points():
    assert set(next_points(Point(0, 0), 5, 5)) == set([Point(0, 1), Point(1, 0)])
    assert set(next_points(Point(1, 1), 5, 5)) == set([Point(1, 0), Point(1, 2), Point(0, 1), Point(2, 1)])


def height(c: str) -> int:
    if c == "S":
        return height("a")
    if c == "E":
        return height("z")
    return ord(c)


def shortest_path(grid: List[List[str]], start: Point) -> int:
    h = []
    path_len = 0
    seen = set()
    heapq.heappush(h, (path_len, start))
    while h:
        path_len, curr_loc = heapq.heappop(h)
        if curr_loc in seen:
            continue
        seen.add(curr_loc)
        curr_height = height(grid[curr_loc.x][curr_loc.y])
        # print(len(h), path_len, curr_loc, curr_height, path_set)
        if grid[curr_loc.x][curr_loc.y] == "E":
            return path_len
        next_pts = next_points(curr_loc, len(grid), len(grid[0]))
        for next_pt in next_pts:
            if next_pt in seen:
                continue
            next_height = height(grid[next_pt.x][next_pt.y])
            if next_height <= curr_height + 1:
                heapq.heappush(h, (path_len + 1, next_pt))
    return -1


def find_start(grid: List[List[str]]) -> Point:
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "S":
                return Point(i, j)
    return Point(0, 0)


def find_possible_starts(grid: List[List[str]]) -> List[Point]:
    starts = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "S" or grid[i][j] == "a":
                starts.append(Point(i, j))
    return starts


def test_sample():
    lines = parse_input(SAMPLE_INPUT)
    grid = [list(line) for line in lines]
    start = find_start(grid)
    l = shortest_path(grid, start)
    print(l)
    assert l == 31

    starts = find_possible_starts(grid)
    min_l = min([shortest_path(grid, p) for p in starts])
    assert min_l == 29


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    lines = parse_input(input_text)
    grid = [list(line) for line in lines]

    # Part 1
    start = find_start(grid)
    l = shortest_path(grid, start)
    print("Part 1: ", l)

    # Part 2
    starts = find_possible_starts(grid)
    possible_paths = [shortest_path(grid, p) for p in starts]

    min_l = min([path_len for path_len in possible_paths if path_len >= 0])
    print("Part 2:", min_l)


if __name__ == "__main__":
    main()