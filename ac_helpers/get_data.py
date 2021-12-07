from aocd.models import Puzzle
import sys
import pathlib

print(sys.argv)


def get_input_data(day):
    fn = pathlib.Path(sys.argv[0]).parent.parent.joinpath('input_data', f"day-{day}.txt")

    try:
        with open(fn) as f:
            return f.read()
    except FileNotFoundError:
        pass

    data = Puzzle(year=2021, day=day).input_data
    with open(fn, "w") as f:
        f.write(data)
    return data
