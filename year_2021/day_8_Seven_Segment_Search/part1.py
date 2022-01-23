from collections import Counter

def run(input_data, day, name):

    c = Counter()

    for in_sig, displays in input_data:
        for display in displays:
            print(display)
            c.update([len(display)])

    # Only digit 1 has 2 segments
    # Only digit 4 has 4 segments
    # Only digit 7 has 3 segments
    # Only digit 8 has 7 segments

    sum_uniquely_defined = c.get(2,0) + c.get(4,0) + c.get(3,0) + c.get(7,0)

    print(f"== Results for day {day} - {name}, part 1.")
    print(f"   {sum_uniquely_defined}")
