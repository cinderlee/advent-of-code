file = open('day7input.txt')

rules = {}

for line in file:
    line = line.strip('\n')
    if "no other bags" in line:
        continue
    parse = line.split(' contain ')
    color_key = parse[0].replace(" bags", '')
    vals = parse[1].split(', ')
    value = {}
    for val in vals:
        lst = val.strip('.').replace('bags', '').replace('bag', '').strip(' ').split(' ')
        num = int(lst[0])
        color = ' '.join(lst[1: ])
        value[color] = num

    rules[color_key] = value

file.close()

lst = []

for key in rules:
    if key != 'shiny gold':
        lst.append([key, [key]])

bags = set()

while len(lst):
    curr_color, path = lst.pop(0)

    if curr_color not in rules:
        continue

    if curr_color in bags:
        for index in range(len(path) - 1):
            bags.add(path[index])
    elif curr_color == 'shiny gold':
        for index in range(len(path) - 1):
            bags.add(path[index])
    else:
        for key in rules[curr_color]:
            lst.append([key, path + [key]])

            
print(len(bags))
