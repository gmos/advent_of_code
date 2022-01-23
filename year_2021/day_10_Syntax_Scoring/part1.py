from collections import deque


def run(nav_lines, day, name):

    EXPECT = {"[": "]", "{": "}", "(": ")", "<": ">"}
    OPENS = set(EXPECT.keys())
    POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}

    def parse_line(line):
        stack = deque()

        for symbol in line:
            if symbol in OPENS:
                stack.append(symbol)
                continue

            if EXPECT[stack.pop()] != symbol:
                # Illegal
                return POINTS[symbol]

        return 0

    result = sum(parse_line(line) for line in nav_lines)

    print(f"== Results for day {day} - {name}, part 1.")
    print(f"   {result=}")
