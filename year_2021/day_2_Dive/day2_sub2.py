def run(input_data):

    movements = [
        (mov_type, int(mov_value))
        for (mov_type, mov_value) in (
            tuple(line.split()) for line in input_data.strip().split("\n")
        )
    ]

    depth = 0
    position = 0
    aim = 0

    for mov_type, mov_value in movements:
        match mov_type:
            case "up":
                aim -= mov_value
            case "down":
                aim += mov_value
            case "forward":
                position += mov_value
                depth += aim * mov_value

    print(f"day2-2: {position=}")
    print(f"day2-2: {depth=}")
    print(f"day2-2: solution={position * depth}")
