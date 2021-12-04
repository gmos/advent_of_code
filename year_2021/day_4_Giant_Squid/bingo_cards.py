class BingoCard:
    """One Bigo card."""

    def __init__(self):
        self.rows = []
        self.row_sets: list[set]
        self.col_sets: list[set]
        self.score = 0

    def fill_from_iterable(self, card_rows):
        """Fill one card from an iterable of blank separated row numbers.
        Stop at empty line
        """

        def parse_card_line(r):
            line = next(r)
            if not line:
                return []
            return [int(x) for x in line.strip().replace("  ", " ").split(" ")]

        row = parse_card_line(card_rows)
        while row:
            self.rows.append(row)
            row = parse_card_line(card_rows)

        self.row_sets = [set(row) for row in self.rows]
        cols = list(map(list, zip(*self.rows)))  # Transpose
        self.col_sets = [set(col) for col in cols]

    def has_bingo(self, last_number_drawn, numbers_drawn):
        """Check card rows and columns against the set of numbers already drawn."""
        if self.score:
            # A card can have Bingo only once
            return False

        for rowcol in self.row_sets + self.col_sets:
            if rowcol.issubset(numbers_drawn):

                self.score = last_number_drawn * sum(
                    set.union(*self.row_sets).difference(numbers_drawn)
                )
                return True
        return False


class BingoDeck:
    """A deck of Bingo cards"""

    def __init__(self):
        self._cards: list[BingoCard] = []
        self.numbers_drawn: set[int] = set()
        self.winning_cards: list[BingoCard] = []

    def add_card(self, card: BingoCard):
        self._cards.append(card)

    def process_new_number(self, number: int):
        self.numbers_drawn.add(number)
        nd = self.numbers_drawn
        for card in self._cards:
            if card.has_bingo(number, nd):
                self.winning_cards.append(card)


def extract(input_data):
    """extract the seqence of numbers drawn and the deck op Bingo cards"""

    def get_numbers(input_lines):
        """Get sequence of numbers drawn"""
        numbers_line = next(input_lines).strip()
        next(input_lines)  # Skip empty line after draws.
        return [int(a) for a in numbers_line.split(",")]

    def get_cards(input_data):
        deck = BingoDeck()
        try:
            while True:
                card = BingoCard()
                card.fill_from_iterable(input_data)
                deck.add_card(card)
        except StopIteration:
            pass
        return deck

    numbers = get_numbers(input_data)
    deck = get_cards(input_data)

    return numbers, deck
