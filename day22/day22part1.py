from collections import deque

FILE_TEST_NM = 'day22testinput.txt'
FILE_NM = 'day22input.txt'
PLAYER_ONE = "Player 1"
PLAYER_TWO = "Player 2"

def determine_winner(player_one_deck, player_two_deck):
    if len(player_one_deck):
        return PLAYER_ONE
    return PLAYER_TWO

def play_combat(player_one_deck, player_two_deck):
    while len(player_one_deck) and len(player_two_deck):
        player_one_card = player_one_deck.popleft()
        player_two_card = player_two_deck.popleft()

        if player_one_card > player_two_card:
            player_one_deck.append(player_one_card)
            player_one_deck.append(player_two_card)
        else:
            player_two_deck.append(player_two_card)
            player_two_deck.append(player_one_card)

    return determine_winner(player_one_deck, player_two_deck)

def parse_cards_from_file(file_nm):
    player_one_cards = deque()
    player_two_cards = deque()
    curr_player = None

    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        if not line:
            continue
        elif PLAYER_ONE in line:
            curr_player = player_one_cards
        elif PLAYER_TWO in line:
            curr_player = player_two_cards
        else:
            curr_player.append(int(line))
    file.close()

    return player_one_cards, player_two_cards

def calculate_score(winning_deck):
    count = len(winning_deck)
    total = 0
    for card in winning_deck:
        total += card * count
        count -= 1
    return total

def solve(file_nm):
    player_one_cards, player_two_cards = parse_cards_from_file(file_nm)
    winner = play_combat(player_one_cards, player_two_cards)
    if winner == PLAYER_ONE:
        return calculate_score(player_one_cards)
    return calculate_score(player_two_cards)

def main():
    assert(solve(FILE_TEST_NM) == 306)
    print(solve(FILE_NM))

main()