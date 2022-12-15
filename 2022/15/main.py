# https://adventofcode.com/2022/day/15
import re
import sys

from utils.files import get_input
from utils.strings import parse_text_as_list
from utils.tests import tests


TEST_1 = [
    ("""
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
    y=10
    """,
     26),
]


# Time complexity: O(k*s); k=max(sensor.x + m_distance) - min(sensor.x-m_distance), s=sensors
# Space complexity: O(s+b); s=sensors, b=beacons
@get_input
@tests(TEST_1)
@parse_text_as_list
def part_1(sensors: list[str]) -> int:
    min_x, max_x, y = sys.maxsize, 0, 2000000
    empty_locations = 0
    beacons = set()
    sensors_reach = dict()
    n = len(sensors)

    r = re.compile(r"Sensor at x=(?P<s_x>-?\d*), y=(?P<s_y>-?\d*): "
                   r"closest beacon is at x=(?P<b_x>-?\d*), y=(?P<b_y>-?\d*)")
    for i in range(n):
        if i == n - 1 and sensors[i].startswith("y="):
            y = int(sensors[i].split("=")[1])
            continue

        m = r.search(sensors[i])
        sensor, beacon = (int(m["s_x"]), int(m["s_y"])), (int(m["b_x"]), int(m["b_y"]))
        m_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        sensors_reach[sensor] = m_distance
        min_x, max_x = min(min_x, sensor[0] - m_distance), max(max_x, sensor[0] + m_distance)
        beacons.add(beacon)

    for x in range(min_x, max_x + 1):
        if (x, y) in beacons:
            continue

        for sensor, m_distance in sensors_reach.items():
            if abs(sensor[0] - x) + abs(sensor[1] - y) <= m_distance:
                empty_locations += 1
                break

    return empty_locations


# Time complexity: O(s^2*d); s=sensors, d=each sensor distance
# Space complexity: O(s+b); s=sensors, b=beacons
@get_input
@parse_text_as_list
def part_2(sensors: list[str]) -> int:
    beacons = set()
    sensors_reach = []

    r = re.compile(r"Sensor at x=(?P<s_x>-?\d*), y=(?P<s_y>-?\d*): "
                   r"closest beacon is at x=(?P<b_x>-?\d*), y=(?P<b_y>-?\d*)")
    for i in range(len(sensors)):
        m = r.search(sensors[i])
        sensor, beacon = (int(m["s_x"]), int(m["s_y"])), (int(m["b_x"]), int(m["b_y"]))
        m_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        sensors_reach.append((*sensor, m_distance))
        beacons.add(beacon)

    for sensor_x, sensor_y, m_distance in sensors_reach:
        for dx in range(m_distance + 2):
            dy = m_distance + 1 - dx

            for sdx, sdy in [(-dx, -dy), (-dx, dy), (dx, -dy), (dx, dy)]:
                x = sensor_x + sdx
                y = sensor_y + sdy

                if 0 > x or x > 4_000_000 or 0 > y or y > 4_000_000:
                    continue

                found = True
                for s_x, s_y, d in sensors_reach:
                    if abs(s_x - x) + abs(s_y - y) <= d:
                        found = False
                        break

                if found:
                    return x * 4_000_000 + y

    return 0


if __name__ == '__main__':
    print(part_1())
    print(part_2())
