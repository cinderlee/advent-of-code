# file = open('day12testinput.txt')
file = open('day12input.txt')

waypt = {
    'x': 10,
    'y': 1
}

ship = {
    'x': 0,
    'y': 0
}

lst = []
for line in file:
    line.strip('\n')
    if line[0] == 'S' or line[0] == 'W':
        lst.append((line[0], int(line[1:]) * -1 ))
    else:
        lst.append((line[0], int(line[1:])))

file.close()

for dir, disp in lst:
    if dir == 'F':
        ship['x'] = ship['x'] + disp * waypt['x']
        ship['y'] = ship['y'] + disp * waypt['y']
    elif dir == 'R' or dir == 'L':
        while disp > 0:
            disp -= 90
            x = waypt['x']
            y = waypt['y']
            if dir == 'R':
                waypt['x'] = y
                waypt['y'] = -1 * x
            else:
                waypt['x'] = -1 * y
                waypt['y'] = x
    else:
        if dir == 'E' or dir == 'W':
            waypt['x'] += disp
        else:
            waypt['y'] += disp

total = abs(ship['x']) + abs(ship['y'])

print(total)