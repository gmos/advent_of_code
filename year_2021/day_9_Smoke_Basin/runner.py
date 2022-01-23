from get_data import get_input_data
import part1
import part2

DAY = 9
NAME = "Smoke Basin"

raw_input_data = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""

raw_input_data = get_input_data(day=DAY).strip()


def parse_row(line):
    """Convert line to list[int] and add edges
    with value 10.
    """
    row = [int(c) for c in line.strip()]
    return [10] + row + [10]


input_lines = raw_input_data.strip().split("\n")
input_matrix = list(parse_row(line) for line in input_lines)
input_matrix = (
    [[10 for x in input_matrix[0]]]
    + input_matrix
    + [[10 for x in input_matrix[-1]]]
)

p1_results = part1.run(input_matrix, DAY, NAME)
part2.run(input_matrix, p1_results, DAY, NAME)
