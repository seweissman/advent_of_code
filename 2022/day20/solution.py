from typing import Union


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node = self
        self.prev: Node = self


def mix(num_list: Node, length: int) -> Node:
    node = num_list
    node_list = []
    for _ in range(length):
        node_list.append(node)
        node = node.next
    for node in node_list:
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
    print_list(sample_list, len(lines))
    mix(sample_list, len(lines))
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
    print_list(sample_list, len(lines))
    mix(sample_list, len(lines))
    g1 = get_index(sample_list, 1000, len(lines))
    assert g1 == 4
    g2 = get_index(sample_list, 2000, len(lines))
    assert g2 == -3
    g3 = get_index(sample_list, 3000, len(lines))
    assert g3 == 2
    assert g1 + g2 + g3 == 3


def print_list(num_list: Node, length: int):
    node = num_list
    values = []
    for _ in range(length):
        values.append(str(node.value))
        node = node.next
    print(", ".join(values))


def build_list(lines) -> Union[Node, None]:
    prev_node = None
    first_node = None
    for line in lines:
        num = int(line)
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
    assert part1_list.value == 6298
    assert part1_list.prev.value == 1868
    print("List length:", length)
    # print_list(part1_list, length)
    mix(part1_list, length)
    g1 = get_index(part1_list, 1000, length)
    g2 = get_index(part1_list, 2000, length)
    g3 = get_index(part1_list, 3000, length)
    print("Part 1", g1 + g2 + g3)


if __name__ == "__main__":
    main()