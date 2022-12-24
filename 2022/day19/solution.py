"""
--- Day 19: Not Enough Minerals ---
Your scans show that the lava did indeed form obsidian!

The wind has changed direction enough to stop sending lava droplets toward you, so you and the elephants exit the cave. As you do, you notice a collection of geodes around the pond. Perhaps you could use the obsidian to create some geode-cracking robots and break them open?

To collect the obsidian from the bottom of the pond, you'll need waterproof obsidian-collecting robots. Fortunately, there is an abundant amount of clay nearby that you can use to make them waterproof.

In order to harvest the clay, you'll need special-purpose clay-collecting robots. To make any type of robot, you'll need ore, which is also plentiful but in the opposite direction from the clay.

Collecting ore requires ore-collecting robots with big drills. Fortunately, you have exactly one ore-collecting robot in your pack that you can use to kickstart the whole operation.

Each robot can collect 1 of its resource type per minute. It also takes one minute for the robot factory (also conveniently from your pack) to construct any type of robot, although it consumes the necessary resources available when construction begins.

The robot factory has many blueprints (your puzzle input) you can choose from, but once you've configured it with a blueprint, you can't change it. You'll need to work out which blueprint is best.

For example:

Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.
(Blueprints have been line-wrapped here for legibility. The robot factory's actual assortment of blueprints are provided one blueprint per line.)

The elephants are starting to look hungry, so you shouldn't take too long; you need to figure out which blueprint would maximize the number of opened geodes after 24 minutes by figuring out which robots to build and when to build them.

Using blueprint 1 in the example above, the largest number of geodes you could open in 24 minutes is 9. One way to achieve that is:

== Minute 1 ==
1 ore-collecting robot collects 1 ore; you now have 1 ore.

== Minute 2 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.

== Minute 3 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
The new clay-collecting robot is ready; you now have 1 of them.

== Minute 4 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
1 clay-collecting robot collects 1 clay; you now have 1 clay.

== Minute 5 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
1 clay-collecting robot collects 1 clay; you now have 2 clay.
The new clay-collecting robot is ready; you now have 2 of them.

== Minute 6 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
2 clay-collecting robots collect 2 clay; you now have 4 clay.

== Minute 7 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
2 clay-collecting robots collect 2 clay; you now have 6 clay.
The new clay-collecting robot is ready; you now have 3 of them.

== Minute 8 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 9 clay.

== Minute 9 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
3 clay-collecting robots collect 3 clay; you now have 12 clay.

== Minute 10 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
3 clay-collecting robots collect 3 clay; you now have 15 clay.

== Minute 11 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 4 clay.
The new obsidian-collecting robot is ready; you now have 1 of them.

== Minute 12 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
3 clay-collecting robots collect 3 clay; you now have 7 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
The new clay-collecting robot is ready; you now have 4 of them.

== Minute 13 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 11 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.

== Minute 14 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 15 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.

== Minute 15 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
4 clay-collecting robots collect 4 clay; you now have 5 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
The new obsidian-collecting robot is ready; you now have 2 of them.

== Minute 16 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 9 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.

== Minute 17 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 13 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.

== Minute 18 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 17 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
The new geode-cracking robot is ready; you now have 1 of them.

== Minute 19 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 21 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 1 open geode.

== Minute 20 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 25 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.

== Minute 21 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 29 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
The new geode-cracking robot is ready; you now have 2 of them.

== Minute 22 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 33 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.

== Minute 23 ==
1 ore-collecting robot collects 1 ore; you now have 5 ore.
4 clay-collecting robots collect 4 clay; you now have 37 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.

== Minute 24 ==
1 ore-collecting robot collects 1 ore; you now have 6 ore.
4 clay-collecting robots collect 4 clay; you now have 41 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.
However, by using blueprint 2 in the example above, you could do even better: the largest number of geodes you could open in 24 minutes is 12.

Determine the quality level of each blueprint by multiplying that blueprint's ID number with the largest number of geodes that can be opened in 24 minutes using that blueprint. In this example, the first blueprint has ID 1 and can open 9 geodes, so its quality level is 9. The second blueprint has ID 2 and can open 12 geodes, so its quality level is 24. Finally, if you add up the quality levels of all of the blueprints in the list, you get 33.

Determine the quality level of each blueprint using the largest number of geodes it could produce in 24 minutes. What do you get if you add up the quality level of all of the blueprints in your list?

--- Part Two ---
While you were choosing the best blueprint, the elephants found some food on their own, so you're not in as much of a hurry; you figure you probably have 32 minutes before the wind changes direction again and you'll need to get out of range of the erupting volcano.

Unfortunately, one of the elephants ate most of your blueprint list! Now, only the first three blueprints in your list are intact.

In 32 minutes, the largest number of geodes blueprint 1 (from the example above) can open is 56. One way to achieve that is:

== Minute 1 ==
1 ore-collecting robot collects 1 ore; you now have 1 ore.

== Minute 2 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.

== Minute 3 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.

== Minute 4 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.

== Minute 5 ==
Spend 4 ore to start building an ore-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
The new ore-collecting robot is ready; you now have 2 of them.

== Minute 6 ==
2 ore-collecting robots collect 2 ore; you now have 3 ore.

== Minute 7 ==
Spend 2 ore to start building a clay-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
The new clay-collecting robot is ready; you now have 1 of them.

== Minute 8 ==
Spend 2 ore to start building a clay-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
1 clay-collecting robot collects 1 clay; you now have 1 clay.
The new clay-collecting robot is ready; you now have 2 of them.

== Minute 9 ==
Spend 2 ore to start building a clay-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
2 clay-collecting robots collect 2 clay; you now have 3 clay.
The new clay-collecting robot is ready; you now have 3 of them.

== Minute 10 ==
Spend 2 ore to start building a clay-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
3 clay-collecting robots collect 3 clay; you now have 6 clay.
The new clay-collecting robot is ready; you now have 4 of them.

== Minute 11 ==
Spend 2 ore to start building a clay-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 10 clay.
The new clay-collecting robot is ready; you now have 5 of them.

== Minute 12 ==
Spend 2 ore to start building a clay-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
5 clay-collecting robots collect 5 clay; you now have 15 clay.
The new clay-collecting robot is ready; you now have 6 of them.

== Minute 13 ==
Spend 2 ore to start building a clay-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
6 clay-collecting robots collect 6 clay; you now have 21 clay.
The new clay-collecting robot is ready; you now have 7 of them.

== Minute 14 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 2 ore.
7 clay-collecting robots collect 7 clay; you now have 14 clay.
The new obsidian-collecting robot is ready; you now have 1 of them.

== Minute 15 ==
2 ore-collecting robots collect 2 ore; you now have 4 ore.
7 clay-collecting robots collect 7 clay; you now have 21 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.

== Minute 16 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
7 clay-collecting robots collect 7 clay; you now have 14 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.
The new obsidian-collecting robot is ready; you now have 2 of them.

== Minute 17 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 2 ore.
7 clay-collecting robots collect 7 clay; you now have 7 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
The new obsidian-collecting robot is ready; you now have 3 of them.

== Minute 18 ==
2 ore-collecting robots collect 2 ore; you now have 4 ore.
7 clay-collecting robots collect 7 clay; you now have 14 clay.
3 obsidian-collecting robots collect 3 obsidian; you now have 7 obsidian.

== Minute 19 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
7 clay-collecting robots collect 7 clay; you now have 7 clay.
3 obsidian-collecting robots collect 3 obsidian; you now have 10 obsidian.
The new obsidian-collecting robot is ready; you now have 4 of them.

== Minute 20 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
2 ore-collecting robots collect 2 ore; you now have 3 ore.
7 clay-collecting robots collect 7 clay; you now have 14 clay.
4 obsidian-collecting robots collect 4 obsidian; you now have 7 obsidian.
The new geode-cracking robot is ready; you now have 1 of them.

== Minute 21 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
2 ore-collecting robots collect 2 ore; you now have 2 ore.
7 clay-collecting robots collect 7 clay; you now have 7 clay.
4 obsidian-collecting robots collect 4 obsidian; you now have 11 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 1 open geode.
The new obsidian-collecting robot is ready; you now have 5 of them.

== Minute 22 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
2 ore-collecting robots collect 2 ore; you now have 2 ore.
7 clay-collecting robots collect 7 clay; you now have 14 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 9 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.
The new geode-cracking robot is ready; you now have 2 of them.

== Minute 23 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
2 ore-collecting robots collect 2 ore; you now have 2 ore.
7 clay-collecting robots collect 7 clay; you now have 21 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 7 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 4 open geodes.
The new geode-cracking robot is ready; you now have 3 of them.

== Minute 24 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
2 ore-collecting robots collect 2 ore; you now have 2 ore.
7 clay-collecting robots collect 7 clay; you now have 28 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 5 obsidian.
3 geode-cracking robots crack 3 geodes; you now have 7 open geodes.
The new geode-cracking robot is ready; you now have 4 of them.

== Minute 25 ==
2 ore-collecting robots collect 2 ore; you now have 4 ore.
7 clay-collecting robots collect 7 clay; you now have 35 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 10 obsidian.
4 geode-cracking robots crack 4 geodes; you now have 11 open geodes.

== Minute 26 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
2 ore-collecting robots collect 2 ore; you now have 4 ore.
7 clay-collecting robots collect 7 clay; you now have 42 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 8 obsidian.
4 geode-cracking robots crack 4 geodes; you now have 15 open geodes.
The new geode-cracking robot is ready; you now have 5 of them.

== Minute 27 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
2 ore-collecting robots collect 2 ore; you now have 4 ore.
7 clay-collecting robots collect 7 clay; you now have 49 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 6 obsidian.
5 geode-cracking robots crack 5 geodes; you now have 20 open geodes.
The new geode-cracking robot is ready; you now have 6 of them.

== Minute 28 ==
2 ore-collecting robots collect 2 ore; you now have 6 ore.
7 clay-collecting robots collect 7 clay; you now have 56 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 11 obsidian.
6 geode-cracking robots crack 6 geodes; you now have 26 open geodes.

== Minute 29 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
2 ore-collecting robots collect 2 ore; you now have 6 ore.
7 clay-collecting robots collect 7 clay; you now have 63 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 9 obsidian.
6 geode-cracking robots crack 6 geodes; you now have 32 open geodes.
The new geode-cracking robot is ready; you now have 7 of them.

== Minute 30 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
2 ore-collecting robots collect 2 ore; you now have 6 ore.
7 clay-collecting robots collect 7 clay; you now have 70 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 7 obsidian.
7 geode-cracking robots crack 7 geodes; you now have 39 open geodes.
The new geode-cracking robot is ready; you now have 8 of them.

== Minute 31 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
2 ore-collecting robots collect 2 ore; you now have 6 ore.
7 clay-collecting robots collect 7 clay; you now have 77 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 5 obsidian.
8 geode-cracking robots crack 8 geodes; you now have 47 open geodes.
The new geode-cracking robot is ready; you now have 9 of them.

== Minute 32 ==
2 ore-collecting robots collect 2 ore; you now have 8 ore.
7 clay-collecting robots collect 7 clay; you now have 84 clay.
5 obsidian-collecting robots collect 5 obsidian; you now have 10 obsidian.
9 geode-cracking robots crack 9 geodes; you now have 56 open geodes.
However, blueprint 2 from the example above is still better; using it, the largest number of geodes you could open in 32 minutes is 62.

You no longer have enough blueprints to worry about quality levels. Instead, for each of the first three blueprints, determine the largest number of geodes you could open; then, multiply these three values together.

Don't worry about quality levels; instead, just determine the largest number of geodes you could open using each of the first three blueprints. What do you get if you multiply these numbers together?
"""

import heapq
import re
from collections import namedtuple
from enum import Enum
from typing import List, Tuple, Union

Cost = namedtuple("Cost", ["ore", "clay", "obsidian"])


class Mineral(str, Enum):
    ORE = "ore"
    CLAY = "clay"
    OBSIDIAN = "obsidian"
    GEODE = "geode"


class Factory:
    def __init__(
        self,
        blueprint: int,
        ore_robot_cost: Cost,
        clay_robot_cost: Cost,
        obsidian_robot_cost: Cost,
        geode_robot_cost: Cost,
    ):
        self.blueprint = blueprint
        self.ore_robot_cost = ore_robot_cost
        self.clay_robot_cost = clay_robot_cost
        self.obsidian_robot_cost = obsidian_robot_cost
        self.geode_robot_cost = geode_robot_cost
        self.ore_robot_ct = 1
        self.clay_robot_ct = 0
        self.obsidian_robot_ct = 0
        self.geode_robot_ct = 0
        self.ore_ct = 0
        self.clay_ct = 0
        self.obsidian_ct = 0
        self.geode_ct = 0

    def can_build_robot(self, mineral: Mineral) -> bool:
        if mineral == Mineral.ORE:
            robot_cost = self.ore_robot_cost
        elif mineral == Mineral.CLAY:
            robot_cost = self.clay_robot_cost
        elif mineral == Mineral.OBSIDIAN:
            robot_cost = self.obsidian_robot_cost
        else:
            robot_cost = self.geode_robot_cost

        return (
            robot_cost.ore <= self.ore_ct
            and robot_cost.clay <= self.clay_ct
            and robot_cost.obsidian <= self.obsidian_ct
        )

    def run_factory(self, robot_to_build: Union[Mineral, None] = None):
        if robot_to_build:
            if robot_to_build == Mineral.ORE:
                robot_cost = self.ore_robot_cost
            elif robot_to_build == Mineral.CLAY:
                robot_cost = self.clay_robot_cost
            elif robot_to_build == Mineral.OBSIDIAN:
                robot_cost = self.obsidian_robot_cost
            else:
                robot_cost = self.geode_robot_cost
            self.ore_ct -= robot_cost.ore
            self.clay_ct -= robot_cost.clay
            self.obsidian_ct -= robot_cost.obsidian
        self.ore_ct += self.ore_robot_ct
        self.clay_ct += self.clay_robot_ct
        self.obsidian_ct += self.obsidian_robot_ct
        self.geode_ct += self.geode_robot_ct
        if robot_to_build:
            if robot_to_build == Mineral.ORE:
                self.ore_robot_ct += 1
            elif robot_to_build == Mineral.CLAY:
                self.clay_robot_ct += 1
            elif robot_to_build == Mineral.OBSIDIAN:
                self.obsidian_robot_ct += 1
            else:
                self.geode_robot_ct += 1

    def get_state(self):
        return (
            self.ore_robot_ct,
            self.clay_robot_ct,
            self.obsidian_robot_ct,
            self.geode_robot_ct,
            self.ore_ct,
            self.clay_ct,
            self.obsidian_ct,
            self.geode_ct,
        )

    def set_state(self, *args):
        (
            self.ore_robot_ct,
            self.clay_robot_ct,
            self.obsidian_robot_ct,
            self.geode_robot_ct,
            self.ore_ct,
            self.clay_ct,
            self.obsidian_ct,
            self.geode_ct,
        ) = args

    @classmethod
    def from_input_line(cls, line: str) -> "Factory":
        def parse_formula(s):
            mineral_amt_strs = s.split(" and ")
            cost = [0, 0, 0]
            minerals = [Mineral.ORE, Mineral.CLAY, Mineral.OBSIDIAN]
            for mineral_amt_str in mineral_amt_strs:
                mineral_amt_str = mineral_amt_str.strip()
                amt_str, mineral_str = mineral_amt_str.split(" ")
                for i, mineral in enumerate(minerals):
                    if mineral_str.startswith(mineral.value):
                        cost[i] = int(amt_str)
            return Cost(*cost)

        bp_str, rest = line.split(": ")
        bp_str = bp_str.split(" ")[1]
        bp = int(bp_str)
        robot_strs = [r.split("costs ")[1] for r in rest.split("Each ") if r]
        ore_str = robot_strs[0]
        ore_cost = parse_formula(ore_str)
        clay_str = robot_strs[1]
        clay_cost = parse_formula(clay_str)
        obsidian_str = robot_strs[2]
        obsidian_cost = parse_formula(obsidian_str)
        geode_str = robot_strs[3]
        geode_cost = parse_formula(geode_str)
        return cls(bp, ore_cost, clay_cost, obsidian_cost, geode_cost)


SAMPLE_INPUT = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""


def test_parse():
    input_lines = parse_input(SAMPLE_INPUT)
    factories: List[Factory] = []
    for input_line in input_lines:
        factories.append(Factory.from_input_line(input_line))
    factory1 = factories[0]
    factory2 = factories[1]
    assert factory1.ore_robot_cost.ore == 4
    assert factory1.clay_robot_cost.ore == 2
    assert factory1.obsidian_robot_cost.ore == 3
    assert factory1.obsidian_robot_cost.clay == 14
    assert factory2.geode_robot_cost.ore == 3
    assert factory2.geode_robot_cost.obsidian == 12


def test_factory():
    ore_robot_cost = Cost(ore=4, clay=0, obsidian=0)
    clay_robot_cost = Cost(ore=2, clay=0, obsidian=0)
    obsidian_robot_cost = Cost(ore=3, clay=14, obsidian=0)
    geode_robot_cost = Cost(ore=2, clay=0, obsidian=7)
    factory = Factory(1, ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost)
    assert factory.can_build_robot(Mineral.ORE) == False
    assert factory.can_build_robot(Mineral.CLAY) == False
    assert factory.can_build_robot(Mineral.OBSIDIAN) == False
    assert factory.can_build_robot(Mineral.GEODE) == False
    factory.run_factory()
    assert factory.ore_ct == 1
    factory.run_factory()
    assert factory.ore_ct == 2
    # Minute 3
    assert factory.can_build_robot(Mineral.CLAY)
    factory.run_factory(Mineral.CLAY)
    # Minute 4
    factory.run_factory()
    assert factory.ore_ct == 2
    assert factory.clay_ct == 1
    # Minte 5 +
    robots = [
        Mineral.CLAY,
        None,
        Mineral.CLAY,
        None,
        None,
        None,
        Mineral.OBSIDIAN,
        Mineral.CLAY,
        None,
        None,
        Mineral.OBSIDIAN,
        None,
        None,
        Mineral.GEODE,
        None,
        None,
        Mineral.GEODE,
        None,
        None,
        None,
    ]
    for i in range(5, 25):
        robot = robots[i - 5]
        if robot:
            factory.run_factory(robot)
        else:
            factory.run_factory()
    assert factory.geode_ct == 9


def score(factory: Factory, time: int):
    ore_in_ore = factory.clay_robot_cost.ore
    clay_in_ore = factory.clay_robot_cost.ore
    obsidian_in_ore = factory.obsidian_robot_cost.clay * clay_in_ore + factory.obsidian_robot_cost.ore
    geode_in_ore = (
        factory.geode_robot_cost.obsidian * obsidian_in_ore
        + factory.geode_robot_cost.clay * clay_in_ore
        + factory.geode_robot_cost.ore
    )
    return (
        -1
        * (
            (factory.ore_ct + factory.ore_robot_ct) * ore_in_ore
            + (factory.clay_ct + factory.clay_robot_ct) * clay_in_ore
            + (factory.obsidian_ct + factory.obsidian_robot_ct) * obsidian_in_ore
            + (factory.geode_ct + factory.geode_robot_ct) * geode_in_ore
        ),
        time,
    )
    # return time
    # return (-1 * (factory.ore_ct + 3 * factory.clay_ct + 5 * factory.obsidian_ct + 7 * factory.geode_ct)
    return (-1 * factory.geode_ct, time, -1 * factory.obsidian_ct, -1 * factory.clay_ct, -1 * factory.ore_ct)


# geode_ct(t) = geode_ct[t-1] + geode_robots[t - 1]
# geode_robots[t] = geode_robots[t-1] + 1 if factory(t-1) has enough materials
# ore_ct(t) = ore_ct(t - 1) -


def find_max(factory: Factory, time_limit=24) -> int:
    geode_ct = 0
    h = []
    curr_set = set()
    curr_set.add(factory.get_state())
    t = 0
    seen = set()
    min_time_to_geode = {}
    while t < time_limit:
        next_set = set()
        print(t, len(curr_set))
        for factory_state in curr_set:
            if factory_state in seen:
                continue
            seen.add(factory_state)

            factory.set_state(*factory_state)

            for mineral in Mineral:
                if factory.can_build_robot(mineral):
                    factory.run_factory(robot_to_build=mineral)
                    next_set.add(factory.get_state())
                    factory.set_state(*factory_state)
            factory.run_factory()
            next_set.add(factory.get_state())

        # Prune states from the set
        curr_set = next_set.copy()
        for factory_state in next_set:
            # Prune any state that doesn't have at least the minimum geode_ct - 2
            # (This was determined by trial and error using the test data.)
            geode_ct = factory_state[-1]
            if geode_ct > 0 and geode_ct not in min_time_to_geode:
                min_time_to_geode[geode_ct] = t
                print(f"Min time to {geode_ct} geodes:", t)
                for other_state in next_set:
                    if other_state[-1] < geode_ct - 2:
                        if other_state in curr_set:
                            curr_set.remove(other_state)
            # Prune any state that we've see
            for i in range(len(factory_state)):
                for v in range(factory_state[i] - 1, -1, -1):
                    l = list(factory_state)
                    l[i] = v
                    worse_state = tuple(l)
                    if worse_state in curr_set:
                        curr_set.remove(worse_state)

        t += 1
    max_geode_ct = 0
    for factory_state in curr_set:
        if factory_state[-1] > max_geode_ct:
            max_geode_ct = factory_state[-1]

    print(max_geode_ct)
    return max_geode_ct


def test_sample_part1():

    input_lines = parse_input(SAMPLE_INPUT)
    factories: List[Factory] = []
    for input_line in input_lines:
        factories.append(Factory.from_input_line(input_line))
    factory1 = factories[0]
    factory2 = factories[1]

    m1 = find_max(factory1)
    assert m1 == 9

    m2 = find_max(factory2)
    assert m2 == 12
    assert m1 * factory1.blueprint + m2 * factory2.blueprint == 33


def test_sample_part2():

    input_lines = parse_input(SAMPLE_INPUT)
    factories: List[Factory] = []
    for input_line in input_lines:
        factories.append(Factory.from_input_line(input_line))
    factory1 = factories[0]
    factory2 = factories[1]

    m1 = find_max(factory1, time_limit=32)
    assert m1 == 56

    m2 = find_max(factory2, time_limit=32)
    assert m2 == 62


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    input_lines = parse_input(input_text)
    quality_score = 0

    for input_line in input_lines:
        factory = Factory.from_input_line(input_line)
        m = find_max(factory)
        quality_score += m * factory.blueprint

    print("Part 1", quality_score)

    factory1 = Factory.from_input_line(input_lines[0])
    m1 = find_max(factory1, time_limit=32)
    factory2 = Factory.from_input_line(input_lines[1])
    m2 = find_max(factory2, time_limit=32)
    factory3 = Factory.from_input_line(input_lines[2])
    m3 = find_max(factory3, time_limit=32)
    print("Part 2:", m1 * m2 * m3)


if __name__ == "__main__":
    main()