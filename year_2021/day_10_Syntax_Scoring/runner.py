from get_data import get_input_data
import part1
import part2

DAY = 10
NAME = "Syntax Scoring"

nav_lines = get_input_data(day=DAY).strip().split('\n')
part1.run(nav_lines, DAY, NAME)
part2.run(nav_lines, DAY, NAME)
