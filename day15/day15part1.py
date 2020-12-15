# file = open('day15testinput.txt')
file = open('day15input.txt')

last_num = None
curr_num = None
spoken = {}
turn = 0
for line in file:
    line = line.strip('\n').split(',')
    for elem in line:
        if curr_num is None:
            curr_num = int(elem)
        else:
            last_num = curr_num
            curr_num = int(elem)
            spoken[last_num] = turn

        turn += 1

file.close()

while turn < 2020:
    if curr_num not in spoken:
        spoken[curr_num] = turn
        curr_num = 0
    else:
        last_turn_spoken = spoken[curr_num]
        spoken[curr_num] = turn 
        curr_num = turn - last_turn_spoken

    turn += 1

print(curr_num)

