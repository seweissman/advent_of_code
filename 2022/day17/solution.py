"""
--- Day 17: Pyroclastic Flow ---
Your handheld device has located an alternative exit from the cave for you and the elephants. The ground is rumbling almost continuously now, but the strange valves bought you some time. It's definitely getting warmer in here, though.

The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are falling into the chamber from above, presumably due to all the rumbling. If you can't work out where the rocks will fall next, you might be crushed!

The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).

For example, suppose this was the jet pattern in your cave:

>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
In jet patterns, < means a push to the left, while > means a push to the right. The pattern above means that the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If the end of the list is reached, it repeats.

The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction indicated by the next symbol in the jet pattern) and then falling one unit down. If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a downward movement would have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.

Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the example above manifests as follows:

The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
+-------+

Jet of gas pushes rock left:
|..@@@@.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|..####.|
+-------+

A new rock begins falling:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|...@...|
|..@@@..|
|...@...|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|..####.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

A new rock begins falling:
|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|...#...|
|..###..|
|...#...|
|..####.|
+-------+
The moment each of the next few rocks begins falling, you would see this:

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|..#....|
|..#....|
|####...|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|..#....|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|.....#.|
|.....#.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|....##.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+
To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks will be 3068 units tall.

How many units tall will the tower of rocks be after 2022 rocks have stopped falling?

--- Part Two ---
The elephants are not impressed by your simulation. They demand to know how tall the tower will be after 1000000000000 rocks have stopped! Only then will they feel confident enough to proceed through the cave.

In the example above, the tower would be 1514285714288 units tall!

How tall will the tower be after 1000000000000 rocks have stopped?
"""
from enum import Enum
from hashlib import md5
from typing import List


class Shape(Enum):
    HORIZONTAL_LINE = 1
    PLUS = 2
    BACKWARDS_ELL = 3
    VERTICAL_LINE = 4
    SQUARE = 5

class Chamber:
    def __init__(self, jet_pattern: str, width=7):
        self.width = 7
        self.jet_pattern = jet_pattern
        self.jet_index = 0
        self.occupied_coords = set()
        self.max_height = -1
        self.max_height_at_last_reset = 0
        self.last_shape = Shape.SQUARE
        self.pattern_buffer = []
        self.rocks_dropped = 0

    def is_occupied(self, x, y):
        if x < 0:
            return True
        if x >= self.width:
            return True
        if y < 0:
            return True
        if (x, y) in self.occupied_coords:
            return True
        return False

    def fill_coord(self, x, y):
        self.occupied_coords.add((x, y))
        if y > self.max_height:
            self.max_height = y

    def next_jet(self):
        p = self.jet_pattern[self.jet_index]
        self.jet_index = (self.jet_index + 1) % len(self.jet_pattern)

        # For part 2, test when the pattern repeats
        if self.jet_index == 0:
            # Compute the state of the chamber since the last reset and store an md5 hash
            # If the hashes match on a future reset, we know we've found a repeating pattern
            s = ""
            for y in range(self.max_height_at_last_reset + 1, self.max_height + 1):
                for x in range(0, self.width):
                    if self.is_occupied(x, y):
                        s += "#"
                    else:
                        s += "."
            h = md5(s.encode("utf8")).hexdigest()
            print(self.rocks_dropped, h, self.max_height - self.max_height_at_last_reset, self.last_shape)
            self.max_height_at_last_reset = self.max_height
            # If we've seen this hash before, set a break point so we can examine the state
            # if h in self.pattern_buffer:
            #     import pdb

            #     pdb.set_trace()
            self.pattern_buffer.append(h)
        return p

    def drop_horiz_line(self):
        """
        ####
        """

        m = self.max_height
        x = 2
        y = m + 4
        while True:
            x = self.jet_horiz_line(x, y)
            if all([not (self.is_occupied(x + i, y - 1)) for i in range(4)]):
                y -= 1
            else:
                break
        for i in range(4):
            self.fill_coord(x + i, y)
        self.last_shape = Shape.HORIZONTAL_LINE

    def jet_horiz_line(self, x_pos, y_pos) -> int:
        p = self.next_jet()
        if p == ">":
            if not self.is_occupied(x_pos + 4, y_pos):
                return x_pos + 1
        if p == "<":
            if not self.is_occupied(x_pos - 1, y_pos):
                return x_pos - 1

        return x_pos

    def drop_plus(self):
        """
        .#.
        ###
        .#.
        """
        m = self.max_height
        # Center of plus
        x = 3
        y = m + 5
        while True:
            x = self.jet_plus(x, y)
            if self.is_occupied(x, y - 2) or self.is_occupied(x - 1, y - 1) or self.is_occupied(x + 1, y - 1):
                break
            else:
                y -= 1
        for d in {-1, 0, 1}:
            self.fill_coord(x + d, y)
            self.fill_coord(x, y + d)
        self.last_shape = Shape.PLUS

    def jet_plus(self, x, y):
        p = self.next_jet()
        if p == ">":
            x_next = x + 1
            if self.is_occupied(x_next, y + 1) or self.is_occupied(x_next, y - 1) or self.is_occupied(x_next + 1, y):
                return x
            return x_next
        if p == "<":
            x_next = x - 1
            if self.is_occupied(x_next, y + 1) or self.is_occupied(x_next, y - 1) or self.is_occupied(x_next - 1, y):
                return x
            return x_next

        return x

    def drop_ell(self):
        """
        ..#
        ..#
        ###
        """
        m = self.max_height
        x = 2
        y = m + 4
        while True:
            x = self.jet_ell(x, y)
            if self.is_occupied(x, y - 1) or self.is_occupied(x + 1, y - 1) or self.is_occupied(x + 2, y - 1):
                break
            else:
                y -= 1
        for d in range(3):
            self.fill_coord(x + d, y)
            self.fill_coord(x + 2, y + d)
        self.last_shape = Shape.BACKWARDS_ELL

    def jet_ell(self, x, y):
        p = self.next_jet()
        if p == ">":
            if self.is_occupied(x + 3, y) or self.is_occupied(x + 3, y + 1) or self.is_occupied(x + 3, y + 2):
                return x
            return x + 1
        if p == "<":
            if self.is_occupied(x - 1, y) or self.is_occupied(x + 1, y + 1) or self.is_occupied(x + 1, y + 2):
                return x
            return x - 1

        return x

    def drop_vert_line(self):
        """
        #
        #
        #
        #
        """
        m = self.max_height
        x = 2
        y = m + 4
        while True:
            x = self.jet_vert_line(x, y)
            if self.is_occupied(x, y - 1):
                break
            else:
                y -= 1
        for d in range(4):
            self.fill_coord(x, y + d)
        self.last_shape = Shape.VERTICAL_LINE

    def jet_vert_line(self, x, y):
        p = self.next_jet()
        if p == ">":
            if (
                self.is_occupied(x + 1, y)
                or self.is_occupied(x + 1, y + 1)
                or self.is_occupied(x + 1, y + 2)
                or self.is_occupied(x + 1, y + 3)
            ):
                return x
            return x + 1
        if p == "<":
            if (
                self.is_occupied(x - 1, y)
                or self.is_occupied(x - 1, y + 1)
                or self.is_occupied(x - 1, y + 2)
                or self.is_occupied(x - 1, y + 3)
            ):
                return x
            return x - 1

        return x

    def drop_square(self):
        """
        ##
        ##
        """
        m = self.max_height
        x = 2
        y = m + 4
        while True:
            x = self.jet_square(x, y)
            if self.is_occupied(x, y - 1) or self.is_occupied(x + 1, y - 1):
                break
            else:
                y -= 1
        self.fill_coord(x, y)
        self.fill_coord(x, y + 1)
        self.fill_coord(x + 1, y)
        self.fill_coord(x + 1, y + 1)
        self.last_shape = Shape.SQUARE

    def jet_square(self, x, y):
        p = self.next_jet()
        if p == ">":
            if self.is_occupied(x + 2, y) or self.is_occupied(x + 2, y + 1):
                return x
            return x + 1
        if p == "<":
            if self.is_occupied(x - 1, y) or self.is_occupied(x - 1, y + 1):
                return x
            return x - 1

        return x

    def drop_next(self):
        if self.last_shape == Shape.SQUARE:
            self.drop_horiz_line()
            # print("drop horiz line")
        elif self.last_shape == Shape.HORIZONTAL_LINE:
            self.drop_plus()
            # print("drop plus")
        elif self.last_shape == Shape.PLUS:
            self.drop_ell()
            # print("drop ell")
        elif self.last_shape == Shape.BACKWARDS_ELL:
            self.drop_vert_line()
            # print("drop vert line")
        elif self.last_shape == Shape.VERTICAL_LINE:
            self.drop_square()
            # print("drop square")
        self.rocks_dropped += 1

    def run_drops(self, n: int = 2022):
        for _ in range(n):
            self.drop_next()
            if all([self.is_occupied(i, self.max_height) for i in range(7)]):
                break
            # chamber.print()

    def print(self):
        for y in range(self.max_height, -1, -1):
            row = "|"
            for x in range(0, self.width):
                if self.is_occupied(x, y):
                    row += "#"
                else:
                    row += "."
            row += "|"
            print(row)
        print("+-------+")


SAMPLE_INPUT = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def test_drops():
    jet_input = parse_input(SAMPLE_INPUT)
    jet_pattern = jet_input[0]
    chamber = Chamber(jet_pattern)
    chamber.drop_horiz_line()
    assert chamber.occupied_coords == {(2, 0), (3, 0), (4, 0), (5, 0)}
    chamber.drop_plus()
    assert chamber.occupied_coords == {(2, 0), (3, 0), (4, 0), (5, 0), (2, 2), (3, 2), (4, 2), (3, 3), (3, 1)}
    chamber.drop_ell()
    chamber.drop_vert_line()
    chamber.drop_square()
    assert (4, 7) in chamber.occupied_coords
    assert (4, 8) in chamber.occupied_coords
    assert (5, 7) in chamber.occupied_coords
    assert (5, 8) in chamber.occupied_coords
    chamber.drop_horiz_line()
    chamber.drop_plus()
    chamber.drop_ell()
    chamber.drop_vert_line()
    chamber.drop_square()
    chamber.print()
    assert chamber.max_height == 16


def test_part1():
    jet_input = parse_input(SAMPLE_INPUT)
    jet_pattern = jet_input[0]
    print(len(jet_pattern))
    chamber = Chamber(jet_pattern)
    chamber.run_drops()
    assert chamber.max_height + 1 == 3068


def test_part2():
    jet_input = parse_input(SAMPLE_INPUT)
    jet_pattern = jet_input[0]
    print("Jet pattern length:", len(jet_pattern))
    chamber = Chamber(jet_pattern)
    chamber.run_drops(n=50)
    h = chamber.max_height
    print("Height at 27:", h)

    #  rocks_dropped, h, max_height, max_height - max_height_at_last_reset, last_shape

    # 8 7d6c4847ef91e2d592efee7e930e3eac 14 14 Shape.BACKWARDS_ELL
    # 14 ad4cd99f0d73cb59b6652af4cea5cb94 22 8 Shape.VERTICAL_LINE
    # 22 7d6e5819868e7b071ac6148febe720d5 38 16 Shape.PLUS
    # 23 - 29 20903d6ac3bc600bfecc3b0a56060b9e 50 12 Shape.VERTICAL_LINE
    # 36 cf12049a132391f283016dae6d1c6d2e 60 10 Shape.HORIZONTAL_LINE
    # 43 1537eb0d52ddcfdf814739683b96c71f 69 9 Shape.BACKWARDS_ELL
    # 49 7ce5f55ee827f16cfa54baf62cbef695 77 8 Shape.VERTICAL_LINE
    # 57 953521d5b666ce4e71162fc037b81c68 91 14 Shape.PLUS
    # 58 - 64 20903d6ac3bc600bfecc3b0a56060b9e 103 12 Shape.VERTICAL_LINE
    # solution.py Jet pattern length: 40

    # For part 1:
    # After the 22th it repeats every 35 drops a pattern of
    # height 12 + 10 + 9 + 8 + 14 = 53
    # 2022 - 22 = 2000
    # 2000 // 35 = 57
    # 2000 % 35 = 5
    # 53 * 57 + height at round 27
    # height at round 27 is 46
    # 3021 + 46 + 1 = 3068

    # For part 2
    # 1000000000000 - 22 = 999999999978
    # 999999999978 // 35 = 28571428570
    # 999999999978 % 35 = 28
    # answer = 53 * 28571428570 + height at round 50 + 1
    # answer = 1514285714288

    # assert chamber.max_height + 1 == 1514285714288


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    jet_input = parse_input(input_text)
    jet_pattern = jet_input[0]
    # Part 1
    chamber = Chamber(jet_pattern)
    chamber.run_drops()
    print("Part 1: ", chamber.max_height + 1)

    # part 2
    # 1756 0469184e958901d209ede3940ff3eae7 2718 2718 Shape.HORIZONTAL_LINE
    # 1757 - 3511 555bb259cb02af5f3bfc6b8c24d6e1c5 5465 2747 Shape.HORIZONTAL_LINE
    # 3512 - 5266 555bb259cb02af5f3bfc6b8c24d6e1c5 8212 2747 Shape.HORIZONTAL_LINE
    # After the 1756th
    # Repeats every 3512 - 1757 = 1755 drops with a height of 2747
    # 1000000000000 - 1756 = 999999998244
    # 999999998244 // 1755 = 569800568
    # 999999998244 % 1755 = 1404
    # answer is 2747 * 569800568 + height at (1404 + 1756)
    # answer is 1565242160296 + height at 3160
    # 1565242160296 + 4904 + 1
    # 1565242165201

    chamber = Chamber(jet_pattern)
    chamber.run_drops(3160)
    print("Height at 3160:", chamber.max_height)


if __name__ == "__main__":
    main()