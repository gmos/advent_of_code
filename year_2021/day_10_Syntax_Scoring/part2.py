from collections import deque


def run(nav_lines, day, name):

    EXPECT = {"[": "]", "{": "}", "(": ")", "<": ">"}
    OPENS = set(EXPECT.keys())
    POINTS = {"(": 1, "[": 2, "{": 3, "<": 4}

    def parse_line(line):
        stack = deque()

        for symbol in line:
            if symbol in OPENS:
                stack.append(symbol)
                continue

            if EXPECT[stack.pop()] != symbol:
                # Illegal line -> no points
                return 0

        completion_score = 0
        for _ in range(len(stack)):
            completion_score = 5 * completion_score + POINTS[stack.pop()]

        return completion_score

    results = []
    for line in nav_lines:
        score = parse_line(line)
        if score:
            results.append(score)

    results = sorted(results)
    print(results)
    result = results[len(results) // 2]

    print(f"== Results for day {day} - {name}, part 2.")
    print(f"   {result=}")
