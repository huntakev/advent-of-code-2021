SAMPLE_INPUT_FILE = "sample_input_day_4_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_4_aoc21.txt"


def unpack_puzzle_input(dir_file: str) -> tuple[list, list]:
    """
    Args:
        dir_file (str): location of .txt file to pull data from

    Returns:
        bingo numbers and bingo cards in list format
    """

    with open(dir_file, "r") as file:
        content = file.read().splitlines()
        bingo_numbers = [int(i) for i in content[0].split(",")]
        bingo_cards = []
        for index in range(2, len(content)):
            if content[index-1] == '':
                bingo_cards.append([[int(i) for i in content[index].split()]])
            elif content[index] != '':
                bingo_cards[-1].append([int(i) for i in content[index].split()])

        return bingo_numbers, bingo_cards


def win_bingo(numbers: list, cards: list) -> tuple[int, int, int, list]:
    """
    Args:
        numbers: bingo numbers to call
        cards: bingo cards to play

    Returns:
        the last number called, the value of uncalled numbers on the winning card, the card score, and the card
    """

    for num in numbers:
        for card in cards:
            sum_uncounted = 0
            for row in range(len(card)):
                for col in range(len(card[row])):
                    if num == card[row][col]:
                        card[row][col] = True
                    elif card[row][col] is not True:
                        sum_uncounted += card[row][col]

            for row in range(len(card)):
                row_counter = 0
                for col in range(len(card[row])):
                    if card[row][col] is True:
                        row_counter += 1
                if row_counter == len(card):
                    return num, sum_uncounted, num * sum_uncounted, card

            for col in range(len(card[0])):
                col_counter = 0
                for row in range(len(card)):
                    if card[row][col] is True:
                        col_counter += 1
                    if col_counter == len(card[0]):
                        return num, sum_uncounted, num * sum_uncounted, card


def lose_bingo(numbers: list, cards: list) -> tuple[int, int, int, list]:
    """
    Args:
        numbers: bingo numbers to call
        cards: bingo cards to play

    Returns:
        the last number called, the value of uncalled numbers on the last winning card, the card score, and the card
    """

    for num in numbers:
        for card in reversed(cards):
            remove_card = False
            sum_uncounted = 0
            for row in range(len(card)):
                for col in range(len(card[row])):
                    if num == card[row][col]:
                        card[row][col] = True
                    elif card[row][col] is not True:
                        sum_uncounted += card[row][col]

            for row in range(len(card)):
                row_counter = 0
                for col in range(len(card[row])):
                    if card[row][col] is True:
                        row_counter += 1
                    if row_counter == len(card):
                        if len(cards) == 1:
                            return num, sum_uncounted, num * sum_uncounted, card
                        remove_card = True

            for col in range(len(card[0])):
                col_counter = 0
                for row in range(len(card)):
                    if card[row][col] is True:
                        col_counter += 1
                    if col_counter == len(card[0]):
                        if len(cards) == 1:
                            return num, sum_uncounted, num * sum_uncounted, card
                        remove_card = True

            if remove_card:
                cards.remove(card)


n, c = unpack_puzzle_input(PUZZLE_INPUT_FILE)
print(win_bingo(n, c))
print(lose_bingo(n, c))
