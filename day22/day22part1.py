from collections import deque

def play_match(cards_one, cards_two):
    while len(cards_one) != 0 and len(cards_two) != 0:
        play_one = cards_one.popleft()
        play_two = cards_two.popleft()

        if play_one > play_two:
            cards_one.append(play_one)
            cards_one.append(play_two)

        else:
            cards_two.append(play_two)
            cards_two.append(play_one)

file = open('day22input.txt', 'r')

player_one = deque()
player_two = deque()
one = True
for line in file:
    line = line.strip('\n')
    if not line:
        continue
    if "Player 1" in line:
        one = True
    elif "Player 2" in line:
        one = False
    elif one:
        player_one.append(int(line))
    else:
        player_two.append(int(line))


file.close()

play_match(player_one, player_two)

winner = None
if len(player_one):
    winner = player_one
else:
    winner = player_two

count = len(winner)
total = 0
for elem in winner:
    total += elem * count
    count -= 1

print(total)