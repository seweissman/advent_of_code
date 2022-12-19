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


"""
from typing import List


class Chamber:
    def __init__(self, jet_pattern: str, width=7):
        self.width = 7
        self.max_heights = []
        self.jet_pattern = jet_pattern
        self.jet_index = 0
        self.occupied_coords = set()
        self.max_height = -1

    def drop_horiz_line(self):
        """
        ####
        """
        m = self.max_height
        x = 2
        y = m + 4
        while True:
            # print(x, y)
            x = self.jet_horiz_line(x, y)
            if all([not (self.is_occupied(x + i, y - 1)) for i in range(3)]):
                y -= 1
            else:
                break
        for i in range(3):
            self.fill_coord(x + i, y)

    def next_jet(self):
        p = self.jet_pattern[self.jet_index]
        self.jet_index = (self.jet_index + 1) % len(self.jet_pattern)
        return p

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

    def jet_horiz_line(self, x_pos, y_pos) -> int:
        p = self.next_jet()
        print(p)
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

    def jet_plus(self, x, y):
        p = self.next_jet()
        print(p)
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

    def jet_ell(self, x, y):
        p = self.next_jet()
        print(p)
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
            print(x, y)
            x = self.jet_vert_line(x, y)
            print("Jet: ", x, y)
            if self.is_occupied(x, y - 1):
                break
            else:
                y -= 1
        for d in range(4):
            self.fill_coord(x, y + d)

    def jet_vert_line(self, x, y):
        p = self.next_jet()
        print(p)
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
            print(x, y)
            x = self.jet_square(x, y)
            print("Jet: ", x, y)
            if self.is_occupied(x, y - 1) or self.is_occupied(x + 1, y - 1):
                break
            else:
                y -= 1
        self.fill_coord(x, y)
        self.fill_coord(x, y + 1)
        self.fill_coord(x + 1, y)
        self.fill_coord(x + 1, y + 1)

    def jet_square(self, x, y):
        p = self.next_jet()
        print(p)
        if p == ">":
            if self.is_occupied(x + 1, y) or self.is_occupied(x + 1, y + 1):
                return x
            return x + 1
        if p == "<":
            if self.is_occupied(x - 1, y) or self.is_occupied(x - 1, y + 1):
                return x
            return x - 1

        return x

    def print(self):
        for y in range(0, self.max_height):
            for x in range(0, self.width):
                pass


SAMPLE_INPUT = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def test_drops():
    jet_input = parse_input(SAMPLE_INPUT)
    jet_pattern = jet_input[0]
    chamber = Chamber(jet_pattern)
    chamber.drop_horiz_line()
    assert chamber.occupied_coords == {(2, 0), (3, 0), (4, 0)}
    chamber.drop_plus()
    assert chamber.occupied_coords == {(2, 0), (3, 0), (4, 0), (2, 2), (3, 2), (4, 2), (3, 3), (3, 1)}
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
    assert chamber.max_height == 16


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()


if __name__ == "__main__":
    main()