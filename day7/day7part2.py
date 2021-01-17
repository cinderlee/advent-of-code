FILE_TEST_NM_1 = 'day7testinput.txt'
FILE_TEST_NM_2 = 'day7testinput2.txt'
FILE_NM = 'day7input.txt'

def parse_line(line):
    '''
    Returns a dictionary representing the rule for one color (line).
    '''
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
    '''
    Returns dictionary of luggage rules read from a file.
    Keys are outer bag colors, values are dictionaries of inner bag colors
    mapped to their specific quantities.
    '''
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
    '''
    Given a inner bag color, returns set of bag colors that are valid
    for the outermost bag. 
    '''
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

def get_number_of_nested_bags(outer_bag_color, rules):
    '''
    Given an outer bag color, returns number of individual bags
    required inside the outer bag.
    '''
    queue = [(outer_bag_color, 1)]
    total_bags = 0

    while len(queue):
        color, num_bags = queue.pop(0)

        if color not in rules:
            continue
        for key in rules[color]:
            total_bags += rules[color][key] * num_bags
            queue.append([key, num_bags * rules[color][key]])
    
    return total_bags


def solve(file_nm):
    rules = read_file_rules(file_nm)
    return get_number_of_nested_bags('shiny gold', rules)

def main():
    assert(solve(FILE_TEST_NM_1) == 32)
    assert(solve(FILE_TEST_NM_2) == 126)
    print(solve(FILE_NM))

main()
