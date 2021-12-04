from collections import Counter


def split_into_lines(input_data: str):
    return input_data.strip().split("\n")


def bit_sieve(candidates, bit_nr_to_sieve):
    split_candidates = {0: [], 1: []}
    for candidate in candidates:
        if candidate[bit_nr_to_sieve] == "1":
            split_candidates[1].append(candidate)
        else:
            split_candidates[0].append(candidate)
    return split_candidates


def select(candidates, bit_nr, test):
    if len(candidates) <= 1:
        return candidates
    split_candidates = bit_sieve(candidates, bit_nr)
    return split_candidates[test(len(split_candidates[0]), len(split_candidates[1]))]


def find_the_buggers(input_lines):
    oxy_candidates = input_lines
    co2_candidates = input_lines

    for bit_nr in range(len(input_lines[0])):
        oxy_candidates = select(
            oxy_candidates, bit_nr, lambda n0, n1: 1 if n1 >= n0 else 0
        )

        co2_candidates = select(
            co2_candidates, bit_nr, lambda n0, n1: 0 if n0 <= n1 else 1
        )

    return int(oxy_candidates[0], 2), int(co2_candidates[0], 2)


def run(input_data, day):

    lines = split_into_lines(input_data)
    oxy_value, co2_value = find_the_buggers(lines)

    print(f"== Results for day {day}, part 2.")
    print(f"   {oxy_value=}")
    print(f"   {co2_value=}")
    print(f"   answer={oxy_value * co2_value}")
