"""
--- Day 20: Grove Positioning System ---
It's finally time to meet back up with the Elves. When you try to contact them, however, you get no reply. Perhaps you're out of range?

You know they're headed to the grove where the star fruit grows, so if you can figure out where that is, you should be able to meet back up with them.

Fortunately, your handheld device has a file (your puzzle input) that contains the grove's coordinates! Unfortunately, the file is encrypted - just in case the device were to fall into the wrong hands.

Maybe you can decrypt it?

When you were still back at the camp, you overheard some Elves talking about coordinate file encryption. The main operation involved in decrypting the file is called mixing.

The encrypted file is a list of numbers. To mix the file, move each number forward or backward in the file a number of positions equal to the value of the number being moved. The list is circular, so moving a number off one end of the list wraps back around to the other end as if the ends were connected.

For example, to move the 1 in a sequence like 4, 5, 6, 1, 7, 8, 9, the 1 moves one position forward: 4, 5, 6, 7, 1, 8, 9. To move the -2 in a sequence like 4, -2, 5, 6, 7, 8, 9, the -2 moves two positions backward, wrapping around: 4, 5, 6, 7, 8, -2, 9.

The numbers should be moved in the order they originally appear in the encrypted file. Numbers moving around during the mixing process do not change the order in which the numbers are moved.

Consider this encrypted file:

1
2
-3
3
-2
0
4
Mixing this file proceeds as follows:

Initial arrangement:
1, 2, -3, 3, -2, 0, 4

1 moves between 2 and -3:
2, 1, -3, 3, -2, 0, 4

2 moves between -3 and 3:
1, -3, 2, 3, -2, 0, 4

-3 moves between -2 and 0:
1, 2, 3, -2, -3, 0, 4

3 moves between 0 and 4:
1, 2, -2, -3, 0, 3, 4

-2 moves between 4 and 1:
1, 2, -3, 0, 3, 4, -2

0 does not move:
1, 2, -3, 0, 3, 4, -2

4 moves between -3 and 0:
1, 2, -3, 4, 0, 3, -2
Then, the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value 0, wrapping around the list as necessary. In the above example, the 1000th number after 0 is 4, the 2000th is -3, and the 3000th is 2; adding these together produces 3.

Mix your encrypted file exactly once. What is the sum of the three numbers that form the grove coordinates?

Your puzzle answer was 2827.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The grove coordinate values seem nonsensical. While you ponder the mysteries of Elf encryption, you suddenly remember the rest of the decryption routine you overheard back at camp.

First, you need to apply the decryption key, 811589153. Multiply each number by the decryption key before you begin; this will produce the actual list of numbers to mix.

Second, you need to mix the list of numbers ten times. The order in which the numbers are mixed does not change during mixing; the numbers are still moved in the order they appeared in the original, pre-mixed list. (So, if -3 appears fourth in the original list of numbers to mix, -3 will be the fourth number to move during each round of mixing.)

Using the same example as above:

Initial arrangement:
811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612

After 1 round of mixing:
0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153

After 2 rounds of mixing:
0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153

After 3 rounds of mixing:
0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459

After 4 rounds of mixing:
0, 1623178306, -2434767459, 811589153, 2434767459, 3246356612, -1623178306

After 5 rounds of mixing:
0, 811589153, -1623178306, 1623178306, -2434767459, 3246356612, 2434767459

After 6 rounds of mixing:
0, 811589153, -1623178306, 3246356612, -2434767459, 1623178306, 2434767459

After 7 rounds of mixing:
0, -2434767459, 2434767459, 1623178306, -1623178306, 811589153, 3246356612

After 8 rounds of mixing:
0, 1623178306, 3246356612, 811589153, -2434767459, 2434767459, -1623178306

After 9 rounds of mixing:
0, 811589153, 1623178306, -2434767459, 3246356612, 2434767459, -1623178306

After 10 rounds of mixing:
0, -2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153
The grove coordinates can still be found in the same way. Here, the 1000th number after 0 is 811589153, the 2000th is 2434767459, and the 3000th is -1623178306; adding these together produces 1623178306.

Apply the decryption key and mix your encrypted file ten times. What is the sum of the three numbers that form the grove coordinates?
"""

from typing import Union


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node = self
        self.prev: Node = self


def mix(num_list: Node, mix_order: list[Node]) -> Node:
    length = len(mix_order)
    for node in mix_order:
        v = node.value

        if abs(v) % length == 0:
            continue
        node_next = node.next
        node_prev = node.prev
        node_next.prev = node_prev
        node_prev.next = node_next
        if v > 0:
            n = node
            for _ in range(v % (length - 1)):
                n = n.next
            assert n != node
            tmp = n.next
            n.next = node
            node.prev = n
            node.next = tmp
            tmp.prev = node
        if v < 0:
            n = node
            for _ in range(abs(v) % (length - 1)):
                n = n.prev
            assert n != node
            tmp = n.prev
            n.prev = node
            node.next = n
            node.prev = tmp
            tmp.next = node
        # print("prev:", node.prev.value)
        # print_list(num_list, length)

    return num_list


def test_mix():
    lines = parse_input(SAMPLE_INPUT)
    sample_list = build_list(lines)

    assert sample_list is not None

    node = sample_list
    mix_order = []
    for _ in range(len(lines)):
        mix_order.append(node)
        node = node.next

    print_list(sample_list, len(lines))
    mix(sample_list, mix_order)
    print_list(sample_list, len(lines))
    assert sample_list.next.value == 2
    assert sample_list.next.next.value == -3
    assert sample_list.next.next.next.value == 4


def get_index(node_list, index, length) -> int:
    zero_node = node_list
    while zero_node.value != 0:
        zero_node = zero_node.next
    for _ in range(index % length):
        zero_node = zero_node.next

    return zero_node.value


def test_part1():
    lines = parse_input(SAMPLE_INPUT)
    sample_list = build_list(lines)
    assert sample_list is not None

    node = sample_list
    mix_order = []
    for _ in range(len(lines)):
        mix_order.append(node)
        node = node.next

    print_list(sample_list, len(lines))
    mix(sample_list, mix_order)
    g1 = get_index(sample_list, 1000, len(lines))
    assert g1 == 4
    g2 = get_index(sample_list, 2000, len(lines))
    assert g2 == -3
    g3 = get_index(sample_list, 3000, len(lines))
    assert g3 == 2
    assert g1 + g2 + g3 == 3


def test_part2():
    lines = parse_input(SAMPLE_INPUT)
    sample_list = build_list(lines, decryption_key=811589153)
    assert sample_list is not None

    node = sample_list
    mix_order = []
    for _ in range(len(lines)):
        mix_order.append(node)
        node = node.next

    print_list(sample_list, len(lines))
    for _ in range(10):
        mix(sample_list, mix_order)
    g1 = get_index(sample_list, 1000, len(lines))
    assert g1 == 811589153
    g2 = get_index(sample_list, 2000, len(lines))
    assert g2 == 2434767459
    g3 = get_index(sample_list, 3000, len(lines))
    assert g3 == -1623178306
    assert g1 + g2 + g3 == 1623178306


def print_list(num_list: Node, length: int):
    node = num_list
    values = []
    for _ in range(length):
        values.append(str(node.value))
        node = node.next
    print(", ".join(values))


def build_list(lines, decryption_key=1) -> Union[Node, None]:
    prev_node = None
    first_node = None
    for line in lines:
        num = int(line) * decryption_key
        node = Node(num)
        if not first_node:
            first_node = node
        if prev_node:
            node.prev = prev_node
            prev_node.next = node
        prev_node = node
    # Link last node to first node
    if prev_node and first_node:
        prev_node.next = first_node
        first_node.prev = prev_node
    return first_node


SAMPLE_INPUT = """
1
2
-3
3
-2
0
4
"""


def test_build_list():
    lines = parse_input(SAMPLE_INPUT)
    sample_list = build_list(lines)
    assert sample_list is not None
    assert sample_list.value == 1
    node = sample_list.next
    assert node.value == 2
    node = node.next
    node = node.next
    node = node.next
    node = node.next
    node = node.next
    node = node.next
    assert node.value == 1


def parse_input(text: str) -> list[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    input_lines = parse_input(input_text)
    part1_list = build_list(input_lines)
    if part1_list is None:
        raise Exception("empty list")

    length = len(input_lines)
    node = part1_list
    mix_order = []
    for _ in range(len(input_lines)):
        mix_order.append(node)
        node = node.next

    assert part1_list.value == 6298
    assert part1_list.prev.value == 1868
    # print_list(part1_list, length)
    mix(part1_list, mix_order)
    g1 = get_index(part1_list, 1000, length)
    g2 = get_index(part1_list, 2000, length)
    g3 = get_index(part1_list, 3000, length)
    print("Part 1", g1 + g2 + g3)

    part2_list = build_list(input_lines, decryption_key=811589153)
    if part2_list is None:
        raise Exception("empty list")

    node = part2_list
    mix_order = []
    for _ in range(len(input_lines)):
        mix_order.append(node)
        node = node.next

    for _ in range(10):
        mix(part2_list, mix_order)

    g1 = get_index(part2_list, 1000, length)
    g2 = get_index(part2_list, 2000, length)
    g3 = get_index(part2_list, 3000, length)
    print("Part 2", g1 + g2 + g3)


if __name__ == "__main__":
    main()