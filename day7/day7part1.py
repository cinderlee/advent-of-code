file = open('day7input.txt')

rules = {}
bags = set()

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
        lst.append([[key], key])

is_seen = set()


while len(lst):
    elem = lst.pop(0)
    path = elem[0]
    curr_color = elem[1]
    if curr_color not in rules:
        continue
    if curr_color in is_seen:
        if curr_color in bags:
            for color_elem in path:
                is_seen.add(color_elem)
                bags.add(color_elem)
        continue
    elif curr_color == 'shiny gold':
        for stuff in elem[0]:
            if stuff != 'shiny gold':
                bags.add(stuff)
                is_seen.add(stuff)
    else:
        for key in rules[curr_color]:
            lst.append([path + [key], key])

            
print(len(bags))
