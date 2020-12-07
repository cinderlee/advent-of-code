file = open('day7input.txt')

rules = {}
bag_total = 0

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

lst = [['shiny gold', 1]]
while (len(lst)):
    elem = lst.pop(0)

    color = elem[0]
    num_bags = elem[1]
    if color not in rules:
        continue
    for key in rules[color]:
        bag_total += rules[color][key] * num_bags
        lst.append([key, num_bags * rules[color][key]])

print(bag_total)