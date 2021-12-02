from ac_get_input_data import get_input_data

input_data = get_input_data(day=1)
input_soundings = [int(s) for s in input_data.strip().split()]

# Part 1
soundings = (s for s in input_soundings)
previous_sounding = next(soundings)
increased = 0

for sounding in soundings:
    increased += 1 if sounding > previous_sounding else 0
    previous_sounding = sounding

print(f"Part 1: {increased=}")

# Part 2

term_1 = (s for s in input_soundings)
term_2 = (s for s in input_soundings[1:])
term_3 = (s for s in input_soundings[2:])
previous_sum = next(term_1) + next(term_2) + next(term_3)
increased = 0
for t3 in term_3:
    current_sum = next(term_1) + next(term_2) + t3
    increased += 1 if current_sum > previous_sum else 0
    previous_sum = current_sum

print(f"Part 2: {increased=}")
