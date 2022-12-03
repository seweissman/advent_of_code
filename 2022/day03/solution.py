"""
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?


"""

from typing import List, Set


def find_overlap(sack: str) -> str:
    comp1_str = sack[0 : len(sack) // 2]
    comp2_str = sack[len(sack) // 2 :]

    comp1_set = set(comp1_str)
    comp2_set = set(comp2_str)
    overlap_set = comp1_set.intersection(comp2_set)
    if len(overlap_set) != 1:
        print(comp1_str, comp2_str, overlap_set)
    assert len(overlap_set) == 1
    overlap_char = list(overlap_set)[0]
    return overlap_char


def test_find_overlap():
    assert find_overlap("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"
    assert find_overlap("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
    assert find_overlap("PmmdzqPrVvPwwTWBwg") == "P"
    assert find_overlap("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn") == "v"
    assert find_overlap("ttgJtRGJQctTZtZT") == "t"
    assert find_overlap("CrZsJsPPZsGzwwsLwLmpwMDw") == "s"


def priority(c: str) -> int:
    if c.lower() == c:
        return ord(c) - ord("a") + 1
    return ord(c) - ord("A") + 27


def test_priority():
    assert priority("p") == 16
    assert priority("L") == 38
    assert priority("P") == 42
    assert priority("v") == 22
    assert priority("t") == 20
    assert priority("s") == 19


def find_sum_priorities(sacks: List[str]) -> int:
    return sum([priority(find_overlap(sack)) for sack in sacks])


SAMPLE_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def test_find_sum_priorities():
    sacks = parse_input(SAMPLE_INPUT)
    assert find_sum_priorities(sacks) == 157


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


if __name__ == "__main__":
    with open("input.txt", encoding="utf8") as file_in:
        lines = parse_input(file_in.read())
    # part 1
    print(find_sum_priorities(lines))
