from bingo_cards import BingoDeck, BingoCard


def run(deck: BingoDeck, numbers: list[int], day, name):

    number_drawn = -1
    for number_drawn in numbers:
        deck.process_new_number(number_drawn)

    print(f"== Results for day {day} - {name}, part 2.")
    if not deck.winning_cards:
        print("   No winning card. Check your code or get your money back!!")
        return

    winning_card = deck.winning_cards[-1]  # Take last
    final_score = winning_card.score
    print(f"   {final_score=}")
