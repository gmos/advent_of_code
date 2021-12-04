from bingo_cards import BingoDeck, BingoCard


def run(deck: BingoDeck, numbers: list[int], day, name):

    number_drawn = -1
    for number_drawn in numbers:
        deck.process_new_number(number_drawn)
        if deck.winning_cards:
            break

    print(f"== Results for day {day} - {name}, part 1.")
    if not deck.winning_cards:
        print("   No winning card. Check your code or get your money back!!")
        return

    winning_card = deck.winning_cards[0]  # Take first if more than one
    final_score = winning_card.score
    print(f"   {final_score=}")
