"""
--- Day 18: Boiling Boulders ---
You and the elephants finally reach fresh air. You've emerged near the base of a large volcano that seems to be actively erupting! Fortunately, the lava seems to be flowing away from you and toward the ocean.

Bits of lava are still being ejected toward you, so you're sheltering in the cavern exit a little longer. Outside the cave, you can see the lava landing in a pond and hear it loudly hissing as it solidifies.

Depending on the specific compounds in the lava and speed at which it cools, it might be forming obsidian! The cooling rate should be based on the surface area of the lava droplets, so you take a quick scan of a droplet as it flies past you (your puzzle input).

Because of how quickly the lava is moving, the scan isn't very good; its resolution is quite low and, as a result, it approximates the shape of the lava droplet with 1x1x1 cubes on a 3D grid, each given as its x,y,z position.

To approximate the surface area, count the number of sides of each cube that are not immediately connected to another cube. So, if your scan were only two adjacent cubes like 1,1,1 and 2,1,1, each cube would have a single side covered and five sides exposed, a total surface area of 10 sides.

Here's a larger example:

2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
In the above example, after counting up all the sides that aren't connected to another cube, the total surface area is 64.

What is the surface area of your scanned lava droplet?

--- Part Two ---
Something seems off about your calculation. The cooling rate depends on exterior surface area, but your calculation also included the surface area of air pockets trapped in the lava droplet.

Instead, consider only cube sides that could be reached by the water and steam as the lava droplet tumbles into the pond. The steam will expand to reach as much as possible, completely displacing any air on the outside of the lava droplet but never expanding diagonally.

In the larger example above, exactly one cube of air is trapped within the lava droplet (at 2,2,5), so the exterior surface area of the lava droplet is 58.


"""

from typing import List, Set, Tuple

Cube = Tuple[int, int, int]


def make_cube_set(input_lines: List[str]) -> Set[Cube]:
    cube_set = set()
    for line in input_lines:
        cube = tuple([int(s) for s in line.split(",")])
        cube_set.add(cube)

    return cube_set


def test_make_cube_set():
    input_lines = parse_input(SAMPLE_INPUT)
    cube_set = make_cube_set(input_lines)
    assert (2, 2, 2) in cube_set
    assert (2, 3, 5) in cube_set
    assert len(cube_set) == 13


def get_adjacent(cube: Cube) -> List[Cube]:
    x, y, z = cube
    return [(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)]


def count_exposed_sides(cube_set: Set[Cube]) -> int:
    exposed_ct = 0
    for cube in cube_set:
        adjacent_cubes = get_adjacent(cube)
        for adj_cube in adjacent_cubes:
            if adj_cube not in cube_set:
                exposed_ct += 1
    return exposed_ct


def test_part_1():
    input_lines = parse_input(SAMPLE_INPUT)
    cube_set = make_cube_set(input_lines)
    assert count_exposed_sides(cube_set) == 64


SAMPLE_INPUT = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    input_lines = parse_input(input_text)
    cube_set = make_cube_set(input_lines)
    exposed_ct = count_exposed_sides(cube_set)
    print("Part 1:", exposed_ct)


if __name__ == "__main__":
    main()