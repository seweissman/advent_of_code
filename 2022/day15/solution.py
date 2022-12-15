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
"""
import re
from collections import namedtuple
from typing import List, Tuple

# x is col, y is row
Point = namedtuple("Point", ["col", "row"])


class Sensor:
    def __init__(self, location: Point, nearest_beacon: Point):
        self.location = location
        self.beacon = nearest_beacon
        self.max_distance = abs(location.col - nearest_beacon.col) + abs(location.row - nearest_beacon.row)

    def distance(self, col: int, row: int):
        return abs(self.location.col - col) + abs(self.location.row - row)

    def in_range_and_not_detected(self, row: int, col: int) -> bool:
        if self.distance(col, row) <= self.max_distance:
            if self.beacon.col != col or self.beacon.row != row:
                return True
        return False


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


def in_range_and_not_detected(row: int, col: int, sensors: List[Sensor]) -> bool:
    for sensor in sensors:
        # print(row, col, sensor.location, sensor.beacon, sensor.distance(col, row), sensor.max_distance)
        if sensor.distance(col, row) <= sensor.max_distance:
            if sensor.beacon.col != col or sensor.beacon.row != row:
                return True
    return False


def count_no_beacons(sensors: List[Sensor], row: int) -> int:
    min_col = min([sensor.location.col - sensor.max_distance for sensor in sensors])
    max_col = max([sensor.location.col + sensor.max_distance for sensor in sensors])
    print("min:", min_col)
    print("max:", max_col)
    no_beacon_pts = set()
    print(len(sensors))
    for sensor in sensors:
        print("Sensor:", sensor.location)
        col_min = sensor.location.col - (sensor.max_distance - abs(sensor.location.row - row))
        col_max = sensor.location.col + (sensor.max_distance - abs(sensor.location.row - row))
        print(col_min, col_max)
        for col in range(col_min, col_max):
            if (row, col) in no_beacon_pts:
                continue
            if in_range_and_not_detected(row, col, sensors):
                no_beacon_pts.add((row, col))
    return len(no_beacon_pts)


def test_sample():
    row = 10
    input_lines = parse_input(SAMPLE_INPUT)
    sensors = [parse_input_line(input_line) for input_line in input_lines]
    no_beacon_ct = count_no_beacons(sensors, row)
    assert no_beacon_ct == 26


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
    no_beacon_ct = count_no_beacons(sensors, row)
    print("Part 1: ", no_beacon_ct)


if __name__ == "__main__":
    main()