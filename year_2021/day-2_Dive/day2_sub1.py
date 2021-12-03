def run(input_data):

    movements = [
        (mov_type, int(mov_value))
        for (mov_type, mov_value) in (
            tuple(line.split()) for line in input_data.strip().split("\n")
        )
    ]
    position = sum(
        mov_amount for mov_type, mov_amount in movements if mov_type == "forward"
    )
    depth = sum(
        mov_amount if mov_type == "down" else -mov_amount
        for mov_type, mov_amount in movements
        if mov_type in ("up", "down")
    )

    print(f"day2-1: {position=}")
    print(f"day2-1: {depth=}")
    print(f"day2-1: solution={position * depth}")
