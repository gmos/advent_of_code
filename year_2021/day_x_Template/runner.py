from get_data import get_input_data
import part1
import part2

DAY = 1
NAME = "ProblemName"

input_data = get_input_data(day=DAY)
part1.run(input_data, DAY, NAME)
part2.run(input_data, DAY, NAME)
