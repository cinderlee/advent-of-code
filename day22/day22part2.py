from collections import deque

def play_match(player_one, player_two):
    hands = set()

    while len(player_one) != 0 and len(player_two) != 0:
        if (tuple(player_one), tuple(player_two)) in hands:
            return "p1"
        hands.add((tuple(player_one), tuple(player_two)))

        winner = None

        play_one = player_one.popleft()
        play_two = player_two.popleft()
        if play_one > play_two:
            winner = 'p1'
        else:
            winner = 'p2'

        if len(player_one) >= play_one and len(player_two) >= play_two:
            new_play_one = deque(player_one[i] for i in range(play_one))
            new_play_two = deque(player_two[i] for i in range(play_two))
            winner = play_match(new_play_one, new_play_two)

        if winner == 'p1':
            player_one.append(play_one)
            player_one.append(play_two)
        else:
            player_two.append(play_two)
            player_two.append(play_one)

    if len(player_one):
        return "p1"
    else:
        return "p2"

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

winner = play_match(player_one, player_two)

if winner == 'p1':
    winner = player_one
else:
    winner = player_two

count = len(winner)
total = 0
for elem in winner:
    total += elem * count
    count -= 1

print(total)