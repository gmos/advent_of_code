from get_data import get_input_data
import part1
import part2

DAY = 7
NAME = "The Treachery of Whales"

input_data = get_input_data(day=DAY)
positions = [int(p) for p in input_data.split(',')]

part1.run(positions, DAY, NAME)
part2.run(positions, DAY, NAME)
