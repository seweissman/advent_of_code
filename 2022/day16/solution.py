"""
--- Day 16: Proboscidea Volcanium ---
The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before the volcano erupts, so you don't have time to go back out the way you came in.

You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's flow rate if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing in labeled AA. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

For example, suppose you had the following scan output:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is 0, so there's no point in opening it. However, you could spend one minute moving to valve BB and another minute opening it; doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional 26 minutes of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing 20 pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing 20 pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing 33 pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.

Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?


"""

import heapq
import re
from enum import Enum
from typing import Dict, Iterable, List, Union


class Valve:
    def __init__(self, name, flow_rate, adjacent: List[str]):
        self.name = name
        self.flow_rate = flow_rate
        self.adjacent = adjacent
        self.dist: Dict[str, int] = dict()
        self.open_time = 10000

    def set_distances(self, dist_map: Dict[str, int]):
        for key, val in dist_map.items():
            start, end = key.split(",")
            if start == self.name and end != self.name and end != "AA":
                self.dist[end] = val

    def open(self, time):
        self.open_time = time

    @classmethod
    def from_input_line(cls, input_line: str) -> "Valve":
        m = re.match("Valve ([A-Z]+) has flow rate=(\d+); tunnels* leads* to valves* ([A-Z, ]+)", input_line)
        if not m:
            raise Exception(f"Could not parse input {input_line}")
        name = m.group(1)
        flow_rate = int(m.group(2))
        adj_str = m.group(3)
        adj_list = adj_str.split(", ")
        return cls(name, flow_rate, adj_list)


def test_valve_creation():
    input_line = "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
    v = Valve.from_input_line(input_line)
    assert v.name == "AA"
    assert v.flow_rate == 0
    assert v.adjacent == ["DD", "II", "BB"]


def make_valves(input_lines: List[str]) -> Dict[str, Valve]:
    valve_map = {}
    for line in input_lines:
        v = Valve.from_input_line(line)
        valve_map[v.name] = v

    valves = valve_map.values()
    non_zero_valves = [v.name for v in valves if v.flow_rate > 0]
    non_zero_valves.append("AA")

    dist = shortest_path_all(valve_map.values())
    dist_nonzero = {}
    for v in non_zero_valves:
        for w in non_zero_valves:
            dist_nonzero[f"{v},{w}"] = dist[f"{v},{w}"]
            dist_nonzero[f"{w},{v}"] = dist[f"{w},{v}"]

    for v in non_zero_valves:
        valve = valve_map[v]
        valve.set_distances(dist_nonzero)
    return valve_map


MAX = 0
IT = 0
from functools import cache


def find_max_flow_elephant(
    valve1: Valve,
    valve2: Valve,
    valve_map: Dict[str, Valve],
    time1=0,
    time2=0,
    max_time=26,
    path1=None,
    path2=None,
    total=0,
    max_to_open=0,
) -> int:
    if path1 is None:
        path1 = []
    if path2 is None:
        path2 = []

    if max_to_open - len(path1) - len(path2) > 2 * max_time - time1 - time2:
        return 0

    if max_to_open == 0:
        for valve in valve_map.values():
            if valve.flow_rate > 0:
                max_to_open += 1

    flow_at_time1 = 0
    for v in path1:
        flow_at_time1 += valve_map[v].flow_rate

    flow_at_time2 = 0
    for v in path2:
        flow_at_time2 += valve_map[v].flow_rate

    valid_adj1 = [
        v
        for v, d in valve1.dist.items()
        if v not in path1 + [valve1.name] and v not in path2 + [valve2.name] and d < max_time - time1
    ]
    valid_adj2 = [
        v
        for v, d in valve2.dist.items()
        if v not in path1 + [valve1.name] and v not in path2 + [valve2.name] and d < max_time - time2
    ]

    if not valid_adj1 and not valid_adj2:
        m = (flow_at_time1 + valve1.flow_rate) * (max_time - time1) + (flow_at_time2 + valve2.flow_rate) * (
            max_time - time2
        )
        global MAX
        global IT
        if total + m > MAX:
            MAX = total + m
        IT = IT + 1
        if IT % 10000 == 0:
            print(time1, time2, total + m, MAX)
        return total + m

    if len(valid_adj1) == 1 and valid_adj1[0] in valid_adj2:
        valid_adj2.remove(valid_adj1[0])

    if not valid_adj1:
        m = max(
            [
                find_max_flow_elephant(
                    valve1,
                    valve_map[v2],
                    valve_map,
                    time1,
                    time2 + valve2.dist[v2] + 1,
                    path1=path1,
                    path2=path2 + [valve2.name],
                    total=total + (flow_at_time2 + valve2.flow_rate) * (valve2.dist[v2] + 1),
                    max_to_open=max_to_open,
                )
                for v2 in valid_adj2
            ]
        )
        return m

    if not valid_adj2:
        m = max(
            [
                find_max_flow_elephant(
                    valve_map[v1],
                    valve2,
                    valve_map,
                    time1 + valve1.dist[v1] + 1,
                    time2,
                    path1=path1 + [valve1.name],
                    path2=path2,
                    total=total + (flow_at_time1 + valve1.flow_rate) * (valve1.dist[v1] + 1),
                    max_to_open=max_to_open,
                )
                for v1 in valid_adj1
            ]
        )
        return m

    m = max(
        [
            find_max_flow_elephant(
                valve_map[v1],
                valve_map[v2],
                valve_map,
                time1 + valve1.dist[v1] + 1,
                time2 + valve2.dist[v2] + 1,
                path1=path1 + [valve1.name],
                path2=path2 + [valve2.name],
                total=total
                + (flow_at_time1 + valve1.flow_rate) * (valve1.dist[v1] + 1)
                + (flow_at_time2 + valve2.flow_rate) * (valve2.dist[v2] + 1),
                max_to_open=max_to_open,
            )
            for v1 in valid_adj1
            for v2 in valid_adj2
            if v1 != v2
        ]
    )
    return m


def find_max_flow(valve: Valve, valve_map: Dict[str, Valve], time=0, max_time=30, path=None) -> int:
    if path is None:
        path = []
    if time > max_time:
        return 0
    flow_at_time = 0
    for v in path:
        flow_at_time += valve_map[v].flow_rate
    valid_adj = [v for v, d in valve.dist.items() if v not in path and d < max_time - time]
    if not valid_adj:
        return (flow_at_time + valve.flow_rate) * (max_time - time)
    m = max(
        [
            (flow_at_time + valve.flow_rate) * (d + 1)
            + find_max_flow(valve_map[v], valve_map, time + d + 1, path=path + [valve.name])
            for v, d in valve.dist.items()
            if v not in path and d < max_time - time
        ]
    )
    return m


def shortest_path_all(valves: Iterable[Valve]):
    dist = {}
    for valve1 in valves:
        for valve2 in valves:
            if valve1.name == valve2.name:
                dist[f"{valve1.name},{valve2.name}"] = 0
            else:
                if valve2.name in valve1.adjacent:
                    dist[f"{valve1.name},{valve2.name}"] = 1
                    dist[f"{valve2.name},{valve1.name}"] = 1
                else:
                    dist[f"{valve1.name},{valve2.name}"] = 100000
                    dist[f"{valve2.name},{valve1.name}"] = 100000

    for valvek in valves:
        for valvei in valves:
            for valvej in valves:

                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[f"{valvei.name},{valvej.name}"] = min(
                    dist[f"{valvei.name},{valvej.name}"],
                    dist[f"{valvei.name},{valvek.name}"] + dist[f"{valvek.name},{valvej.name}"],
                )
                dist[f"{valvej.name},{valvei.name}"] = dist[f"{valvei.name},{valvej.name}"]
    return dist


SAMPLE_INPUT = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


def test_sample_part1():
    lines = parse_input(SAMPLE_INPUT)
    valve_map = make_valves(lines)

    max_flow = find_max_flow(valve_map["AA"], valve_map)
    assert max_flow == 1651


def test_sample_part2():
    lines = parse_input(SAMPLE_INPUT)
    valve_map = make_valves(lines)
    max_flow = find_max_flow_elephant(valve_map["AA"], valve_map["AA"], valve_map)
    global MAX
    MAX = 0
    assert max_flow == 1707


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    lines = parse_input(input_text)
    valve_map = make_valves(lines)

    # max_flow = find_max_flow(valve_map["AA"], valve_map)
    # print("Part 1:", max_flow)

    max_flow = find_max_flow_elephant(valve_map["AA"], valve_map["AA"], valve_map)
    print("Part 2:", max_flow)


if __name__ == "__main__":
    main()