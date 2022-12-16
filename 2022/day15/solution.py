"""
--- Day 15: Beacon Exclusion Zone ---
You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of deployable sensors that you imagine were originally built to locate lost Elves.

The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.

Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer coordinates. Each sensor knows its own position and can determine the position of a beacon precisely; however, sensors can only lock on to the one beacon closest to the sensor as measured by the Manhattan distance. (There is never a tie where two beacons are the same distance to a sensor.)

It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:

Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, the closest beacon to it is at 10,16.

Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at 8,7:

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer (in any positions marked #).

None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress beacon is by working out where it isn't. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.

So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where y=10, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:

                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
10 ..####B######################..
11 .###S#############.###########.
In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.

Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a beacon?

--- Part Two ---
Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.

Find the only possible position for the distress beacon. What is its tuning frequency?


"""
import re
from collections import namedtuple
from typing import List, Tuple, Union

# x is col, y is row
Point = namedtuple("Point", ["col", "row"])


class Sensor:
    def __init__(self, location: Point, nearest_beacon: Point):
        self.location = location
        self.beacon = nearest_beacon
        self.max_distance = abs(location.col - nearest_beacon.col) + abs(location.row - nearest_beacon.row)

    def distance(self, col: int, row: int):
        return abs(self.location.col - col) + abs(self.location.row - row)


def parse_input_line(line: str) -> Sensor:
    m = re.match(f".*x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)", line)
    if m:
        sensor_loc = Point(int(m.group(1)), int(m.group(2)))
        beacon_loc = Point(int(m.group(3)), int(m.group(4)))
        sensor = Sensor(sensor_loc, beacon_loc)
        return sensor
    raise Exception(f"Could not parse input {line}")


def test_parse_input_line():
    line = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
    sensor = parse_input_line(line)
    assert sensor.location.col == 2
    assert sensor.location.row == 18
    assert sensor.max_distance == 7

    line = "Sensor at x=8, y=7: closest beacon is at x=2, y=10"
    sensor = parse_input_line(line)
    assert sensor.location.col == 8
    assert sensor.location.row == 7
    assert sensor.max_distance == 9


SAMPLE_INPUT = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


class Range:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __repr__(self):
        return f"[{self.low}, {self.high}]"

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Range):
            return False
        return self.low == __o.low and self.high == __o.high


def combine_ranges(ranges: List[Range]) -> List[Range]:
    changed = True
    new_ranges = []
    for i in range(len(ranges)):
        changed = False
        r = ranges[i]
        for j in range(i + 1, len(ranges)):
            other_r = ranges[j]
            # ...[r.low   r.high]...
            # ......[o.low    o.high]...
            if r.low <= other_r.low and r.high >= other_r.low - 1:
                ranges[j].low = r.low
                ranges[j].high = max(r.high, other_r.high)
                changed = True
                break
            # .......[r.low     r.high]...
            # ...[o.low    o.high]...
            elif r.low - 1 <= other_r.high and r.high >= other_r.high:
                ranges[j].low = min(r.low, other_r.low)
                ranges[j].high = r.high
                changed = True
                break
            elif r.low <= other_r.low and r.high >= other_r.high:
                ranges[j].low = r.low
                ranges[j].high = r.high
                changed = True
            elif other_r.low <= r.low and other_r.high >= r.high:
                changed = True

        if not changed:
            new_ranges.append(r)
    return new_ranges


def test_combine_ranges():
    assert combine_ranges([Range(0, 5), Range(2, 8), Range(3, 4)]) == [Range(0, 8)]
    assert combine_ranges([Range(0, 1), Range(3, 4)]) == [Range(0, 1), Range(3, 4)]


def sum_ranges(ranges: List[Range]) -> int:
    range_sum = 0
    for r in ranges:
        range_sum += r.high - r.low

    return range_sum


def get_no_beacon_ranges(
    sensors: List[Sensor], row: int, col_min: Union[int, None] = None, col_max: Union[int, None] = None
) -> List[Range]:

    ranges = []
    for sensor in sensors:
        sensor_col_min = sensor.location.col - (sensor.max_distance - abs(sensor.location.row - row))
        if col_min is not None:
            sensor_col_min = max(sensor_col_min, col_min)
        sensor_col_max = sensor.location.col + (sensor.max_distance - abs(sensor.location.row - row))
        if col_max is not None:
            sensor_col_max = min(col_max, sensor_col_max)
        if sensor_col_min < sensor_col_max:
            ranges.append(Range(sensor_col_min, sensor_col_max))
    # print("Ranges:", ranges)

    # print("Combined ranges: ", combine_ranges(ranges))

    combined_ranges = combine_ranges(ranges)
    return combined_ranges


def test_sample_part1():
    row = 10
    input_lines = parse_input(SAMPLE_INPUT)
    sensors = [parse_input_line(input_line) for input_line in input_lines]
    no_beacon_ranges = get_no_beacon_ranges(sensors, row)
    no_beacon_ct = sum_ranges(no_beacon_ranges)
    assert no_beacon_ct == 26


def test_sample_part2():
    input_lines = parse_input(SAMPLE_INPUT)
    sensors = [parse_input_line(input_line) for input_line in input_lines]

    for row in range(20):
        no_beacon_ranges = get_no_beacon_ranges(sensors, row, col_min=0, col_max=20)
        if len(no_beacon_ranges) > 1:
            assert len(no_beacon_ranges) == 2
            r1, r2 = no_beacon_ranges
            print(r1, r2)
            missing_col = (max(r1.low, r2.low) + min(r1.high, r2.high)) // 2
            assert missing_col == 14
            assert missing_col * 4000000 + row == 56000011


def parse_input(text: str) -> List[str]:
    """Parse lines of input from raw text"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines


def main():
    with open("input.txt", encoding="utf8") as file_in:
        input_text = file_in.read()
    input_lines = parse_input(input_text)
    sensors = [parse_input_line(input_line) for input_line in input_lines]
    row = 2000000
    no_beacon_ranges = get_no_beacon_ranges(sensors, row)
    no_beacon_ct = sum_ranges(no_beacon_ranges)
    print("Part 1: ", no_beacon_ct)

    for row in range(4000000):
        no_beacon_ranges = get_no_beacon_ranges(sensors, row, col_min=0, col_max=4000000)
        if len(no_beacon_ranges) > 1:
            r1, r2 = no_beacon_ranges
            missing_col = (max(r1.low, r2.low) + min(r1.high, r2.high)) // 2
            print("Part 2", missing_col * 4000000 + row)


if __name__ == "__main__":
    main()