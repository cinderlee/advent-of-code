# file = open('day12testinput.txt')
file = open('day12input.txt')

values = {
    'E': 0,
    'W': 0,
    'N': 0,
    'S': 0
}

next_r = {
    'E': 'S',
    'W': 'N',
    'N': 'E',
    'S': 'W'
}

next_l = {
    'E': 'N',
    'W': 'S',
    'N': 'W',
    'S': 'E'
}

curr = 'E'

lst = []
for line in file:
    line.strip('\n')
    lst.append((line[0], int(line[1:]) ))

file.close()

# print(lst)

for dir, disp in lst:
    if dir == 'F':
        values[curr] += disp
    elif dir == 'R' or dir == 'L':
        while disp > 0:
            if dir == 'R':
                curr = next_r[curr]
            else:
                curr = next_l[curr]
            disp -= 90
    else:
        values[dir] += disp

total = abs(values['E'] - values['W']) + abs(values['N'] - values['S'])

print(total)