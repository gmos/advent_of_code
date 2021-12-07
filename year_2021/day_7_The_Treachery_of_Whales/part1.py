def run(positions, day, name):

    min_pos = min(positions)
    max_pos = max(positions)
    best_position = min_pos
    best_fuel_consumption = len(positions) * (max_pos - min_pos)
    for test_position in range(min_pos, max_pos + 1):
        fuel_consumption = sum(
            abs(crab_position - test_position) for crab_position in positions
        )
        if fuel_consumption < best_fuel_consumption:
            best_fuel_consumption = fuel_consumption
            best_position = test_position

    print(f"== Results for day {day} - {name}, part 1.")
    print(f"   {best_fuel_consumption=} for {best_position=}")
