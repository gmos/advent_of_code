from get_data import get_input_data
import part1
import part2

DAY = 8
NAME = "Seven Segment Search"

input_data = get_input_data(day=DAY)
input_lines = (x.strip() for x in input_data.split("\n"))
input_data = [
    (tuple(d[0].split(" ")), tuple(d[1].split(" ")))
    for d in (s.split(" | ") for s in input_lines)
]
# print(input_data[:4])
part1.run(input_data, DAY, NAME)
# part2.run(input_data, DAY, NAME)
