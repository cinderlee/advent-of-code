FILE_TEST_NM = 'day7testinput.txt'
FILE_NM = 'day7input.txt'

def parse_line(line):
    color_key, rules = line.split(' contain ' )
    color_key = color_key.replace(" bags", '')
    rules = rules.strip('.').split(', ')
    rules_dict = {}
    for rule in rules:
        rule = rule.replace('bags', '').replace('bag', '').strip(' ').split(' ')
        bag_count = int(rule[0])
        bag_color = ' '.join(rule[1:])
        rules_dict[bag_color] = bag_count
    return {color_key: rules_dict}

def read_file_rules(file_nm):
    file = open(file_nm, 'r')
    rules = {}

    for line in file:
        line = line.strip('\n')
        if "no other bags" in line:
            continue
        rules.update(parse_line(line))

    file.close()
    return rules

def get_outer_bag_colors(inner_bag_color, rules):
    queue = []

    for key in rules:
        if key != inner_bag_color:
            queue.append([key, [key]])

    bags = set()

    while len(queue):
        curr_color, path = queue.pop(0)

        if curr_color not in rules:
            continue

        if curr_color in bags or curr_color == inner_bag_color:
            for index in range(len(path) - 1):
                bags.add(path[index])
        else:
            for key in rules[curr_color]:
                queue.append([key, path + [key]])

    return bags

def solve(file_nm):
    rules = read_file_rules(file_nm)
    return len(get_outer_bag_colors('shiny gold', rules))

def main():
    assert(solve(FILE_TEST_NM) == 4)
    print(solve(FILE_NM))

main()
