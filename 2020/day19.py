# Day 19: Monster Messages

INPUT_FILE_NAME = "./inputs/day19input.txt"
TEST_FILE_NAME = "./inputs/day19testinput.txt"
TEST_FILE_NAME_2 = "./inputs/day19testinput2.txt"

def read_file(file_nm):
    '''
    Returns a list of rules and a list of messages read from a file.
    '''
    rules = []
    messages = []
    is_rules = True

    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        if not line:
            is_rules = False
        elif is_rules:
            rules.append(line)
        else:
            messages.append(line)
    file.close()

    return rules, messages

def add_and_parse_rule(line, rules, is_part_two):
    '''
    Parses a rule and stores the rule in the rules dictionary.
    Keys are the rule numbers and values are a list of sub rules
    or strings.

    For part two, rules 8 and 11 are modified to be the following:
        8: 42 | 42 8
        11: 42 31 | 42 11 31
    '''
    key, val = line.split(':')
    if '|' in val:
        val_lst = []
        for elem in val.split("|"):
            elem = elem.strip(' ').split(' ')
            val_lst.append(elem)
        rules[key] = val_lst
    elif '"' in val:
        rules[key] = val.strip(' "')
    else:
        rules[key] = val.strip(' ').split(' ')
        if is_part_two:
            if key == '8':
                rules[key] = [rules[key], ['42', '8']]
            elif key == '11':
                rules[key] = [rules[key], ['42', '11', '31']]

def parse_rules_lst(rules_lst, is_part_two=False):
    '''
    Returns a dictionary of rules given the list of rules in string format.
    '''
    rules = {}
    for rule in rules_lst:
        add_and_parse_rule(rule, rules, is_part_two)
    return rules

def check_valid_loop(rules, rule, rule_part):
    '''
    Returns whether the loop for rule 8 or 11 were completed.
    '''
    find_key = None
    if rule in rules['8']:
        find_key = '8'
    elif rule in rules['11']:
        find_key = '11'
    else:
        return False
    
    if rule == rules[find_key][0]:  # didn't finish non-loop possibility
        return False
    elif rule_part != rules[find_key][-1][-1]: # didn't finish loop section
        return False
    return True

def check_rule(rules, rule, string, index, is_part_two):
    for elem in rule:
        if is_part_two and index >= len(string):
            return check_valid_loop(rules, rule, elem), index

        sub_rule = rules[elem]
        if isinstance(sub_rule, str):
            if string[index] == sub_rule:
                index += 1
            else:
                return False, index
        else:
            result = False
            if isinstance(sub_rule[0], list):
                for elem in sub_rule:
                    res, new_index = check_rule(rules, elem, string, index, is_part_two)
                    result = result | res
                    if result:
                        index = new_index
                        break
            else:
                result, new_index = check_rule(rules, sub_rule, string, index, is_part_two)
                if result:
                    index = new_index
            if not result:
                return result, index
    return True, index

def count_valid_matches(rules, messages, rule_num, is_part_two=False):
    '''
    Returns the total of valid messages that match a rule number.
    '''
    count = 0
    for message in messages:
        res, index = check_rule(rules, rules[str(rule_num)], message, 0, is_part_two)
        if res and index == len(message):
            count += 1
    return count

def solve_part_one(rules_lst, messages):
    rules = parse_rules_lst(rules_lst)
    return count_valid_matches(rules, messages, 0)

def solve_part_two(rules_lst, messages):
    rules = parse_rules_lst(rules_lst, True)
    return count_valid_matches(rules, messages, 0, True)

def main():
    test_rules_lst, test_messages = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_rules_lst, test_messages) == 2)

    test_rules_lst_2, test_messages_2 = read_file(TEST_FILE_NAME_2)
    assert(solve_part_two(test_rules_lst_2, test_messages_2) == 12)

    rules_lst, messages = read_file(INPUT_FILE_NAME)
    print(solve_part_one(rules_lst, messages))
    print(solve_part_two(rules_lst, messages))

main()
