"""
--- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:

Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8
min(8,4) - max(6,2) + 1 = 4 - 6 + 1 = -1

.23......  2-3
...45....  4-5
min(5,3) - max(4,2) + 1 = 3 - 4 + 1 = 0

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

min(8,7) - max(3,2) + 1 = 7-3+1 = 5

.....6...  6-6
...456...  4-6
min(6,6) - max(6,4) + 1 = 6 - 6 + 1 = 1

.23456...  2-6
...45678.  4-8
Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

"""

from collections import namedtuple
from typing import Callable, List, Tuple

Range = namedtuple("Range", ["low", "high"])


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def convert_to_range(range_str: str) -> Range:
    range_low, range_high = range_str.split("-")
    return Range(int(range_low), int(range_high))


def partially_overlap(range1: Range, range2: Range) -> bool:
    if range1.high < range2.low or range2.high < range1.low:
        return False
    return True


def completely_overlap(range1: Range, range2: Range) -> bool:
    if range1.low >= range2.low and range1.high <= range2.high:
        return True
    if range2.low >= range1.low and range2.high <= range1.high:
        return True
    return False


def count_overlaps(input_text: str, overlap_fn: Callable[[Range, Range], bool]) -> int:
    lines = parse_input(input_text)
    overlap_count = 0
    for line in lines:
        range1_str, range2_str = line.split(",")
        range1 = convert_to_range(range1_str)
        range2 = convert_to_range(range2_str)
        if overlap_fn(range1, range2):
            overlap_count += 1
    return overlap_count


SAMPLE_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_sample_input_part1():
    assert count_overlaps(SAMPLE_INPUT, overlap_fn=completely_overlap) == 2


def test_sample_input_part2():
    assert count_overlaps(SAMPLE_INPUT, overlap_fn=partially_overlap) == 4

if __name__ == "__main__":
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()

    # part 1
    print("Part1: ", count_overlaps(input_text, overlap_fn=completely_overlap))

    # part 2
    print("Part2: ", count_overlaps(input_text, overlap_fn=partially_overlap))