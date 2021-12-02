from aocd.models import Puzzle
import json


def get_input_data(day):
    try:
        with open(f"day-{day}.txt") as f:
            return f.read()
    except FileNotFoundError:
        pass

    data = Puzzle(year=2021, day=day).input_data
    with open(f"day-{day}.txt", "w") as f:
        f.write(data)
    return data
