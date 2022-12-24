"""
--- Day 21: Monkey Math ---
The monkeys are back! You're worried they're going to try to steal your stuff again, but it seems like they're just holding their ground and making various monkey noises at you.

Eventually, one of the elephants realizes you don't speak monkey and comes over to interpret. As it turns out, they overheard you talking about trying to find the grove; they can show you a shortcut if you answer their riddle.

Each monkey is given a job: either to yell a specific number or to yell the result of a math operation. All of the number-yelling monkeys know their number from the start; however, the math operation monkeys need to wait for two other monkeys to yell a number, and those two other monkeys might also be waiting on other monkeys.

Your job is to work out the number the monkey named root will yell before the monkeys figure it out themselves.

For example:

root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
Each line contains the name of a monkey, a colon, and then the job of that monkey:

A lone number means the monkey's job is simply to yell that number.
A job like aaaa + bbbb means the monkey waits for monkeys aaaa and bbbb to yell each of their numbers; the monkey then yells the sum of those two numbers.
aaaa - bbbb means the monkey yells aaaa's number minus bbbb's number.
Job aaaa * bbbb will yell aaaa's number multiplied by bbbb's number.
Job aaaa / bbbb will yell aaaa's number divided by bbbb's number.
So, in the above example, monkey drzm has to wait for monkeys hmdt and zczc to yell their numbers. Fortunately, both hmdt and zczc have jobs that involve simply yelling a single number, so they do this immediately: 32 and 2. Monkey drzm can then yell its number by finding 32 minus 2: 30.

Then, monkey sjmn has one of its numbers (30, from monkey drzm), and already has its other number, 5, from dbpl. This allows it to yell its own number by finding 30 multiplied by 5: 150.

This process continues until root yells a number: 152.

However, your actual situation involves considerably more monkeys. What number will the monkey named root yell?

--- Part Two ---
Due to some kind of monkey-elephant-human mistranslation, you seem to have misunderstood a few key details about the riddle.

First, you got the wrong job for the monkey named root; specifically, you got the wrong math operation. The correct operation for monkey root should be =, which means that it still listens for two numbers (from the same two monkeys as before), but now checks that the two numbers match.

Second, you got the wrong monkey for the job starting with humn:. It isn't a monkey - it's you. Actually, you got the job wrong, too: you need to figure out what number you need to yell so that root's equality check passes. (The number that appears after humn: in your input is now irrelevant.)

In the above example, the number you need to yell to pass root's equality test is 301. (This causes root to get the same number, 150, from both of its monkeys.)

"""

import re


def proc_line(line):
    monkey, formula = line.split(": ")
    try:
        int(formula)
        return (monkey, [], formula)
    except ValueError:
        pass
    m = re.match("([a-z]+).* [-+/*] ([a-z]+)", formula)
    if not m:
        raise Exception(f"Couldn't parse {formula}")
    else:
        return (monkey, [m.group(1), m.group(2)], formula)


def proc_line_part2(line):
    monkey, formula = line.split(": ")
    if monkey == "humn":
        return None
    try:
        int(formula)
        return (monkey, [], formula)
    except ValueError:
        pass
    m = re.match("([a-z]+).* [-+/*] ([a-z]+)", formula)
    if not m:
        raise Exception(f"Couldn't parse {formula}")
    else:
        if monkey == "root":
            return (monkey, [m.group(1), m.group(2)], f"{m.group(1)} == {m.group(2)}")

        return (monkey, [m.group(1), m.group(2)], formula)


SAMPLE_INPUT = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""


def test_proc_line():
    proc_line("root: pppw + sjmn")


def parse_input(text: str) -> list[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def find_monkey_values(lines):
    monkey_vals = {}
    monkeys = [proc_line(line) for line in lines]
    while "root" not in monkey_vals:
        for monkey in monkeys:
            name, dependencies, formula = monkey
            if name in monkey_vals:
                continue
            if all([dep_name in monkey_vals for dep_name in dependencies]):
                for dep_name in dependencies:
                    formula = formula.replace(dep_name, str(monkey_vals[dep_name]))
                monkey_vals[name] = eval(formula)
    return int(monkey_vals["root"])


def is_str_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def simplify_monkey_values(lines):
    monkey_vals = {}
    monkeys = [proc_line_part2(line) for line in lines]
    monkeys = [m for m in monkeys if m is not None]
    for monkey in monkeys:
        name, dependencies, formula = monkey
        monkey_vals[name] = (set(dependencies), formula)

    changed = True
    while changed:
        changed = False
        for name, (dependencies, formula) in monkey_vals.items():
            formula_new = formula
            dependencies_new = set()
            for dep_name in dependencies:
                if dep_name in monkey_vals:
                    dep_dependencies, dep_formula = monkey_vals[dep_name]
                    for dep_dependency in dep_dependencies:
                        dependencies_new.add(dep_dependency)

                    if is_str_int(dep_formula):
                        formula_new = formula_new.replace(dep_name, f"{dep_formula}")
                    else:
                        formula_new = formula_new.replace(dep_name, f"({dep_formula})")
                else:
                    dependencies_new.add(dep_name)
            if formula != formula_new:
                # print("updated formula:", formula, formula_new)
                monkey_vals[name] = (dependencies_new, formula_new)
                changed = True
        # print("Changed:", monkey_vals)
    # print(monkey_vals)

    return monkey_vals["root"]


def test_part1():
    lines = parse_input(SAMPLE_INPUT)
    root_val = find_monkey_values(lines)
    assert root_val == 152


def test_part2():
    lines = parse_input(SAMPLE_INPUT)
    root_formula = simplify_monkey_values(lines)
    formula = simplify_formula(root_formula[1])
    print("Simplified: ", formula)
    # ((4 + (2 * (humn - 3))) / 4) == 150
    # human = 301


def simplify_formula(formula: str) -> str:
    changed = True
    while changed:
        changed = False
        m = re.match(r".*(\(-?\d+ [-+/*] -?\d+\)).*", formula)
        if m:
            formula = formula.replace(m.group(1), str(int(eval(m.group(1)))))
            changed = True
    return formula

def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    input_lines = parse_input(input_text)
    root_val = find_monkey_values(input_lines)
    print("Part 1:", root_val)

    root_formula = simplify_monkey_values(input_lines)
    formula = simplify_formula(root_formula[1])
    print("Simplified: ", formula)

    # Do the rest manually
    """
((452 + ((88019559115041 - ((((((541 + (((((4 * ((((((((2 * (((((557 + ((996 + (((((261 + (2 * ((2 * (((980 + ((39 * (934 + ((((((((((191 + (6 * ((2 * (((((978 + (3 * (((((humn - 259) / 5) + 998) * 50) - 222))) / 12) + 442) / 2) - 274)) - 560))) + 105) / 2) - 556) * 2) + 65) + 773) / 2) - 791) / 9))) + 703)) / 9) - 848)) - 760))) + 658) / 3) - 888) * 4)) / 8)) / 2) - 436) * 11) + 798)) - 585) / 5) + 225) * 2) - 318) / 2) + 564)) - 998) / 3) - 362) / 4)) * 7) + 344) / 5) - 275) * 6)) / 3)) * 2)
== 24376746909942
==>
humn 
== (693940982052 - 998)*5 + 259

    """


if __name__ == "__main__":
    main()