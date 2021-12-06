from collections import Counter
from get_data import get_input_data
import part1
import part2

DAY = 6
NAME = "Lanternfish"

input_data = get_input_data(day=DAY)
fish_counts = Counter(int(c) for c in input_data.strip().split(","))

part1.run(fish_counts, DAY, NAME)
part2.run(fish_counts, DAY, NAME)
