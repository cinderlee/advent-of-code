from collections import deque

FILE_TEST_NM = 'day22testinput.txt'
FILE_NM = 'day22input.txt'
PLAYER_ONE = "Player 1"
PLAYER_TWO = "Player 2"

def create_sub_hand(deck, num_cards):
    '''
    Returns a sub-deck of n cards from given deck
    '''
    return deque([deck[i] for i in range(num_cards)])

def determine_winner(player_one_deck):
    '''
    Determines who the winner is from Player 1's deck. If Player 1 has cards,
    that means Player 2's deck is empty and Player 1 wins. Otherwise,
    Player 1's deck is empty and Player 2 wins.
    '''
    if len(player_one_deck):
        return PLAYER_ONE
    return PLAYER_TWO

def play_recursive_combat(player_one_deck, player_two_deck):
    '''
    Player 1 and Player 2 play a game of Recursive Combat, where the first number in the deck
    represents the top of the deck.

    How the game of Recursive Combat works:
        Before drawing cards, if there was a previous round where the decks have 
        the same cards in the same order as the current round, player 1 wins to prevent
        infinite games. Rounds of other games (recursive sub-games) are excluded.

        Both players draw their top card. If players have at least as many cards
        in their deck as the value of the drawn card, the winner is the winner of 
        the next game of Recursive Combat. Otherwise, the winner is the player
        who drew the higher card. The winner's card is placed above the other card.

        The game ends when a player has all of the cards.

    Returns the winner.
    '''
    seen_decks = set()

    while len(player_one_deck) and len(player_two_deck):
        decks = (tuple(player_one_deck), tuple(player_two_deck))
        if decks in seen_decks:
            return PLAYER_ONE
        seen_decks.add(decks)

        player_one_card = player_one_deck.popleft()
        player_two_card = player_two_deck.popleft()
        winner = None

        if len(player_one_deck) >= player_one_card and len(player_two_deck) >= player_two_card:
            player_one_sub_deck = create_sub_hand(player_one_deck, player_one_card)
            player_two_sub_deck = create_sub_hand(player_two_deck, player_two_card)
            winner = play_recursive_combat(player_one_sub_deck, player_two_sub_deck)
        elif player_one_card > player_two_card:
            winner = PLAYER_ONE
        else:
            winner = PLAYER_TWO

        if winner == PLAYER_ONE:
            player_one_deck.append(player_one_card)
            player_one_deck.append(player_two_card)
        else:
            player_two_deck.append(player_two_card)
            player_two_deck.append(player_one_card)

    return determine_winner(player_one_deck)

def parse_cards_from_file(file_nm):
    '''
    Returns two decks of cards for Player 1 and Player 2 from a file.
    '''
    player_one_cards = deque()
    player_two_cards = deque()
    curr_deck = None

    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        if not line:
            continue
        elif PLAYER_ONE in line:
            curr_deck = player_one_cards
        elif PLAYER_TWO in line:
            curr_deck = player_two_cards
        else:
            curr_deck.append(int(line))
    file.close()

    return player_one_cards, player_two_cards

def calculate_score(winning_deck):
    '''
    Calculates the winner's score. The bottom card in the deck is worth the card value 
    multiplied by 1, the second-to-last card is worth the value multiplied by 2, and so on.
    '''
    count = len(winning_deck)
    total = 0
    for card in winning_deck:
        total += card * count
        count -= 1
    return total

def solve(file_nm):
    '''
    Returns the winning score after two players play Combat.
    '''
    player_one_cards, player_two_cards = parse_cards_from_file(file_nm)
    winner = play_recursive_combat(player_one_cards, player_two_cards)
    if winner == PLAYER_ONE:
        return calculate_score(player_one_cards)
    return calculate_score(player_two_cards)

def main():
    assert(solve(FILE_TEST_NM) == 291)
    print(solve(FILE_NM))


main()