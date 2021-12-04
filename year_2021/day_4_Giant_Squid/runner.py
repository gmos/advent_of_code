from get_data import get_input_data
from bingo_cards import extract
import part1
import part2

DAY = 4
NAME = "ProblemName"

input_lines = (line for line in get_input_data(day=DAY).split("\n"))
numbers, deck = extract(input_lines)

part1.run(deck, numbers, DAY, NAME)
part2.run(deck, numbers, DAY, NAME)
