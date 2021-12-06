from dataclasses import dataclass


@dataclass
class Fishes:
    fish_count: int
    cycle_count: int = 8  # Default are newly born fish

    def cycle_advance(self) -> int:
        """Advances the cycle for this group and returns the number of newly borns."""
        self.cycle_count = self.cycle_count - 1
        if self.cycle_count < 0:
            self.cycle_count = 6
            return self.fish_count
        return 0
