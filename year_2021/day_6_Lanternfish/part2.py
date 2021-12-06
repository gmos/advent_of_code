from collections import Counter

from fish import Fishes

SIMULATION_DAYS = 256


def run(initial_fish_counts: Counter, day, name):
    simulation_fish_tank = [Fishes(c, n) for n, c in initial_fish_counts.items()]

    for _ in range(SIMULATION_DAYS):
        born = 0
        for fishes in simulation_fish_tank:
            born += fishes.cycle_advance()
        simulation_fish_tank.append(Fishes(born))

    total_fishes = sum([fishes.fish_count for fishes in simulation_fish_tank])

    print(f"== Results for day {day} - {name}, part 2.")
    print(f"   {total_fishes=}")
