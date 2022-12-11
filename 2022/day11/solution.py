"""
--- Day 11: Monkey in the Middle ---
As you finally start making your way upriver, you realize your pack is much lighter than you remember. Just then, one of the items from your pack goes flying overhead. Monkeys are playing Keep Away with your missing things!

To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation, you realize the monkeys operate based on how worried you are about each item.

You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items, and how the monkey makes decisions based on your worry level. For example:

Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
Each monkey has several attributes:

Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
Test shows how the monkey uses your worry level to decide where to throw an item next.
If true shows what happens with an item if the Test was true.
If false shows what happens with an item if the Test was false.
After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item causes your worry level to be divided by three and rounded down to the nearest integer.

The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items it is holding one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn. The process of each monkey taking a single turn is called a round.

When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.

In the above example, the first round proceeds as follows:

Monkey 0:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by 19 to 1501.
    Monkey gets bored with item. Worry level is divided by 3 to 500.
    Current worry level is not divisible by 23.
    Item with worry level 500 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 98.
    Worry level is multiplied by 19 to 1862.
    Monkey gets bored with item. Worry level is divided by 3 to 620.
    Current worry level is not divisible by 23.
    Item with worry level 620 is thrown to monkey 3.
Monkey 1:
  Monkey inspects an item with a worry level of 54.
    Worry level increases by 6 to 60.
    Monkey gets bored with item. Worry level is divided by 3 to 20.
    Current worry level is not divisible by 19.
    Item with worry level 20 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 65.
    Worry level increases by 6 to 71.
    Monkey gets bored with item. Worry level is divided by 3 to 23.
    Current worry level is not divisible by 19.
    Item with worry level 23 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 75.
    Worry level increases by 6 to 81.
    Monkey gets bored with item. Worry level is divided by 3 to 27.
    Current worry level is not divisible by 19.
    Item with worry level 27 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 6 to 80.
    Monkey gets bored with item. Worry level is divided by 3 to 26.
    Current worry level is not divisible by 19.
    Item with worry level 26 is thrown to monkey 0.
Monkey 2:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by itself to 6241.
    Monkey gets bored with item. Worry level is divided by 3 to 2080.
    Current worry level is divisible by 13.
    Item with worry level 2080 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 60.
    Worry level is multiplied by itself to 3600.
    Monkey gets bored with item. Worry level is divided by 3 to 1200.
    Current worry level is not divisible by 13.
    Item with worry level 1200 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 97.
    Worry level is multiplied by itself to 9409.
    Monkey gets bored with item. Worry level is divided by 3 to 3136.
    Current worry level is not divisible by 13.
    Item with worry level 3136 is thrown to monkey 3.
Monkey 3:
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 3 to 77.
    Monkey gets bored with item. Worry level is divided by 3 to 25.
    Current worry level is not divisible by 17.
    Item with worry level 25 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 500.
    Worry level increases by 3 to 503.
    Monkey gets bored with item. Worry level is divided by 3 to 167.
    Current worry level is not divisible by 17.
    Item with worry level 167 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 620.
    Worry level increases by 3 to 623.
    Monkey gets bored with item. Worry level is divided by 3 to 207.
    Current worry level is not divisible by 17.
    Item with worry level 207 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 1200.
    Worry level increases by 3 to 1203.
    Monkey gets bored with item. Worry level is divided by 3 to 401.
    Current worry level is not divisible by 17.
    Item with worry level 401 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 3136.
    Worry level increases by 3 to 3139.
    Monkey gets bored with item. Worry level is divided by 3 to 1046.
    Current worry level is not divisible by 17.
    Item with worry level 1046 is thrown to monkey 1.
After round 1, the monkeys are holding items with these worry levels:

Monkey 0: 20, 23, 27, 26
Monkey 1: 2080, 25, 167, 207, 401, 1046
Monkey 2: 
Monkey 3: 
Monkeys 2 and 3 aren't holding any items at the end of the round; they both inspected items during the round and threw them all before the round ended.

This process continues for a few more rounds:

After round 2, the monkeys are holding items with these worry levels:
Monkey 0: 695, 10, 71, 135, 350
Monkey 1: 43, 49, 58, 55, 362
Monkey 2: 
Monkey 3: 

After round 3, the monkeys are holding items with these worry levels:
Monkey 0: 16, 18, 21, 20, 122
Monkey 1: 1468, 22, 150, 286, 739
Monkey 2: 
Monkey 3: 

After round 4, the monkeys are holding items with these worry levels:
Monkey 0: 491, 9, 52, 97, 248, 34
Monkey 1: 39, 45, 43, 258
Monkey 2: 
Monkey 3: 

After round 5, the monkeys are holding items with these worry levels:
Monkey 0: 15, 17, 16, 88, 1037
Monkey 1: 20, 110, 205, 524, 72
Monkey 2: 
Monkey 3: 

After round 6, the monkeys are holding items with these worry levels:
Monkey 0: 8, 70, 176, 26, 34
Monkey 1: 481, 32, 36, 186, 2190
Monkey 2: 
Monkey 3: 

After round 7, the monkeys are holding items with these worry levels:
Monkey 0: 162, 12, 14, 64, 732, 17
Monkey 1: 148, 372, 55, 72
Monkey 2: 
Monkey 3: 

After round 8, the monkeys are holding items with these worry levels:
Monkey 0: 51, 126, 20, 26, 136
Monkey 1: 343, 26, 30, 1546, 36
Monkey 2: 
Monkey 3: 

After round 9, the monkeys are holding items with these worry levels:
Monkey 0: 116, 10, 12, 517, 14
Monkey 1: 108, 267, 43, 55, 288
Monkey 2: 
Monkey 3: 

After round 10, the monkeys are holding items with these worry levels:
Monkey 0: 91, 16, 20, 98
Monkey 1: 481, 245, 22, 26, 1092, 30
Monkey 2: 
Monkey 3: 

...

After round 15, the monkeys are holding items with these worry levels:
Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
Monkey 1: 110, 36
Monkey 2: 
Monkey 3: 

...

After round 20, the monkeys are holding items with these worry levels:
Monkey 0: 10, 12, 14, 26, 34
Monkey 1: 245, 93, 53, 199, 115
Monkey 2: 
Monkey 3: 
Chasing all of the monkeys at once is impossible; you're going to have to focus on the two most active monkeys if you want any hope of getting your stuff back. Count the total number of times each monkey inspects items over 20 rounds:

Monkey 0 inspected items 101 times.
Monkey 1 inspected items 95 times.
Monkey 2 inspected items 7 times.
Monkey 3 inspected items 105 times.
In this example, the two most active monkeys inspected items 101 and 105 times. The level of monkey business in this situation can be found by multiplying these together: 10605.

Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?


--- Part Two ---
You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another way to keep your worry levels manageable.

At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!

With these new rules, you can still figure out the monkey business after 10000 rounds. Using the same example above:

== After round 1 ==
Monkey 0 inspected items 2 times.
Monkey 1 inspected items 4 times.
Monkey 2 inspected items 3 times.
Monkey 3 inspected items 6 times.

== After round 20 ==
Monkey 0 inspected items 99 times.
Monkey 1 inspected items 97 times.
Monkey 2 inspected items 8 times.
Monkey 3 inspected items 103 times.

== After round 1000 ==
Monkey 0 inspected items 5204 times.
Monkey 1 inspected items 4792 times.
Monkey 2 inspected items 199 times.
Monkey 3 inspected items 5192 times.

== After round 2000 ==
Monkey 0 inspected items 10419 times.
Monkey 1 inspected items 9577 times.
Monkey 2 inspected items 392 times.
Monkey 3 inspected items 10391 times.

== After round 3000 ==
Monkey 0 inspected items 15638 times.
Monkey 1 inspected items 14358 times.
Monkey 2 inspected items 587 times.
Monkey 3 inspected items 15593 times.

== After round 4000 ==
Monkey 0 inspected items 20858 times.
Monkey 1 inspected items 19138 times.
Monkey 2 inspected items 780 times.
Monkey 3 inspected items 20797 times.

== After round 5000 ==
Monkey 0 inspected items 26075 times.
Monkey 1 inspected items 23921 times.
Monkey 2 inspected items 974 times.
Monkey 3 inspected items 26000 times.

== After round 6000 ==
Monkey 0 inspected items 31294 times.
Monkey 1 inspected items 28702 times.
Monkey 2 inspected items 1165 times.
Monkey 3 inspected items 31204 times.

== After round 7000 ==
Monkey 0 inspected items 36508 times.
Monkey 1 inspected items 33488 times.
Monkey 2 inspected items 1360 times.
Monkey 3 inspected items 36400 times.

== After round 8000 ==
Monkey 0 inspected items 41728 times.
Monkey 1 inspected items 38268 times.
Monkey 2 inspected items 1553 times.
Monkey 3 inspected items 41606 times.

== After round 9000 ==
Monkey 0 inspected items 46945 times.
Monkey 1 inspected items 43051 times.
Monkey 2 inspected items 1746 times.
Monkey 3 inspected items 46807 times.

== After round 10000 ==
Monkey 0 inspected items 52166 times.
Monkey 1 inspected items 47830 times.
Monkey 2 inspected items 1938 times.
Monkey 3 inspected items 52013 times.
After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, the level of monkey business in this situation is now 2713310158.

Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?
"""

from collections import deque
from typing import Callable, List, Tuple


class Monkey:
    def __init__(
        self,
        starting_items: List[int],
        operation: Callable[[int], int],
        divisor: int,
        success_monkey: int,
        failure_monkey: int,
        worry_factor: int = 3,
    ):
        self.items = deque(starting_items)
        self.operation = operation
        self.divisor = divisor
        self.success_monkey = success_monkey
        self.failure_monkey = failure_monkey
        self.inspection_ct = 0
        self.worry_factor = worry_factor

    def inspect_and_pass(self) -> Tuple[int, int]:
        if len(self.items) == 0:
            return -1, -1
        self.inspection_ct += 1
        item = self.items.popleft()
        value = self.operation(item) // self.worry_factor
        test_result = value % self.divisor == 0
        if test_result:
            return value, self.success_monkey
        return value, self.failure_monkey

    def add_item(self, item: int):
        self.items.append(item)

    def get_items(self) -> List[int]:
        return list(self.items)

    @classmethod
    def make_monkey(cls, input_lines: List[str], worry_factor: int = 3) -> "Monkey":
        starting_line = input_lines[0]
        items_str = starting_line.split(": ")[1]
        items = [int(item) for item in items_str.split(", ")]
        operation_line = input_lines[1]
        operation_str = operation_line.split("old ")[1]
        operator_str = operation_str[0]
        operand_str = operation_str.split(" ")[1]
        if operand_str == "old":
            if operator_str == "+":
                operation = lambda x: x + x
            elif operator_str == "*":
                operation = lambda x: x * x
            else:
                raise Exception(f"unknown operator {operator_str}")
        else:
            operand = int(operand_str)
            if operator_str == "+":
                operation = lambda x: x + operand
            elif operator_str == "*":
                operation = lambda x: x * operand
            else:
                raise Exception(f"unknown operator {operator_str}")

        test_line = input_lines[2]
        divisor_str = test_line.split(" by ")[1]
        divisor = int(divisor_str)
        true_line = input_lines[3]
        true_monkey = int(true_line.split("monkey ")[1])
        false_line = input_lines[4]
        false_monkey = int(false_line.split("monkey ")[1])
        return cls(items, operation, divisor, true_monkey, false_monkey, worry_factor=worry_factor)


SAMPLE_INPUT = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def get_monkeys(lines: List[str], worry_factor: int = 3) -> List[Monkey]:
    monkeys = []
    monkey_lines = []
    for line in lines:
        if line.startswith("Monkey"):
            if len(monkey_lines) > 0:
                monkey = Monkey.make_monkey(monkey_lines, worry_factor=worry_factor)
                monkeys.append(monkey)
                monkey_lines = []
        else:
            monkey_lines.append(line)
    if monkey_lines:
        last_monkey = Monkey.make_monkey(monkey_lines, worry_factor=worry_factor)
        monkeys.append(last_monkey)
    return monkeys


def test_get_monkeys():
    input_lines = parse_input(SAMPLE_INPUT)
    monkeys = get_monkeys(input_lines)
    assert len(monkeys) == 4


def test_make_monkey():
    lines = parse_input(SAMPLE_INPUT)
    monkey_lines = lines[1:6]
    monkey = Monkey.make_monkey(monkey_lines)
    assert monkey.get_items() == [79, 98]
    assert monkey.operation(79) == 79 * 19
    assert monkey.divisor == 23
    assert monkey.failure_monkey == 3
    assert monkey.success_monkey == 2


def run_round(monkeys: List[Monkey], use_lcm=False):
    # We know that monkey divisors are all prime so lcm is the product
    lcm = 1
    for monkey in monkeys:
        lcm = monkey.divisor * lcm
    for monkey in monkeys:
        while True:
            value, pass_monkey_index = monkey.inspect_and_pass()
            if pass_monkey_index < 0:
                break
            if use_lcm:
                value = value % lcm
            monkeys[pass_monkey_index].add_item(value)


def monkey_business(monkeys: List[Monkey]) -> int:
    cts = [monkey.inspection_ct for monkey in monkeys]
    cts.sort()
    return cts[-1] * cts[-2]


def test_part1():
    input_lines = parse_input(SAMPLE_INPUT)
    monkeys = get_monkeys(input_lines)
    run_round(monkeys)
    assert monkeys[0].get_items() == [20, 23, 27, 26]
    assert monkeys[1].get_items() == [2080, 25, 167, 207, 401, 1046]
    assert len(monkeys[2].get_items()) == 0
    assert len(monkeys[3].get_items()) == 0
    for _ in range(19):
        run_round(monkeys)
    assert monkeys[0].get_items() == [10, 12, 14, 26, 34]
    assert monkeys[1].get_items() == [245, 93, 53, 199, 115]
    assert len(monkeys[2].get_items()) == 0
    assert len(monkeys[3].get_items()) == 0
    assert monkeys[0].inspection_ct == 101
    assert monkeys[1].inspection_ct == 95
    assert monkeys[2].inspection_ct == 7
    assert monkeys[3].inspection_ct == 105
    assert monkey_business(monkeys) == 10605


def test_part2():
    input_lines = parse_input(SAMPLE_INPUT)
    monkeys = get_monkeys(input_lines, worry_factor=1)
    run_round(monkeys, use_lcm=True)
    assert monkeys[0].inspection_ct == 2
    assert monkeys[1].inspection_ct == 4
    assert monkeys[2].inspection_ct == 3
    assert monkeys[3].inspection_ct == 6
    for _ in range(19):
        run_round(monkeys, use_lcm=True)
    assert monkeys[0].inspection_ct == 99
    assert monkeys[1].inspection_ct == 97
    assert monkeys[2].inspection_ct == 8
    assert monkeys[3].inspection_ct == 103
    for i in range(10000 - 20):
        run_round(monkeys, use_lcm=True)
    assert monkeys[0].inspection_ct == 52166
    assert monkeys[1].inspection_ct == 47830
    assert monkeys[2].inspection_ct == 1938
    assert monkeys[3].inspection_ct == 52013


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    lines = parse_input(input_text)
    monkeys = get_monkeys(lines)
    for _ in range(20):
        run_round(monkeys)
    print("Part 1:", monkey_business(monkeys))
    monkeys = get_monkeys(lines, worry_factor=1)
    for _ in range(10000):
        run_round(monkeys, use_lcm=True)

    print("Part 2:", monkey_business(monkeys))


if __name__ == "__main__":
    main()
