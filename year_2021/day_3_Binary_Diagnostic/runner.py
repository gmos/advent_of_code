from get_data import get_input_data
import part1
import part2

DAY = 3

input_data = get_input_data(day=DAY)
part1.run(input_data, DAY)
part2.run(input_data, DAY)
