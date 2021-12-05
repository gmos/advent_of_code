from get_data import get_input_data
from plane import Point, Line
import part1
import part2

DAY = 5
NAME = "Hydrothermal Venture"

# Not much time today, we have Sinterklaas today.
# So decided for simple, brute force approach.
# Plane dimension is 1000 * 1000. Too large for a full matrix of 1M Counters.
# So used a sparse dict of touched points only, just containing the count.

input_data = get_input_data(day=DAY)
input_line_data = input_data.strip().replace(" ", "").replace("->", ",").split("\n")
lines = [
    Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
    for x1, y1, x2, y2 in (in_line.split(",") for in_line in input_line_data)
]

part1.run(lines, DAY, NAME)
part2.run(lines, DAY, NAME)
