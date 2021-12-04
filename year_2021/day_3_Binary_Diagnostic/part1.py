from collections import Counter


def split_into_lines(input_data: str):
    return input_data.strip().split("\n")


class DiagnosticAccumulator:
    def __init__(self, sample_line):
        self.n_samples = 0
        self.n_bits = len(sample_line)
        self.bit_counters = {}
        for bit_number, _ in enumerate(sample_line):
            self.bit_counters[bit_number] = Counter()

    def add_reading(self, line):
        self.n_samples += 1
        for bit_number, bit_value in enumerate(line):
            self.bit_counters[bit_number].update(bit_value)

    def _evaluate(self, test):
        result = 0
        for k, v in self.bit_counters.items():
            result |= test(v.get("0", 0), v.get("1", 0)) << (self.n_bits - k - 1)
        return result

    def gamma_rate(self):
        return self._evaluate(lambda n0, n1: 1 if n1 > n0 else 0)

    def epsilon_rate(self):
        return self._evaluate(lambda n0, n1: 0 if n1 > n0 else 1)


def run(input_data, day):

    lines = split_into_lines(input_data)

    accu = DiagnosticAccumulator(lines[0])
    for line in lines:
        accu.add_reading(line)

    gamma_rate = accu.gamma_rate()
    epsilon_rate = accu.epsilon_rate()

    print(f"== Results for day {day}, part 1.")
    print(f"   {gamma_rate=}")
    print(f"   {epsilon_rate=}")
    print(f"   answer={epsilon_rate*gamma_rate}")
