def add_and_parse_rule(line, rules):
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
        if key == '8':
            rules[key] = [rules[key], ['42', '8']]
        elif key == '11':
            rules[key] = [rules[key], ['42', '11', '31']]

def check_valid_loop(rules, rule, rule_part):
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

def check_rule(rules, rule, string, index):
    for elem in rule:
        if index >= len(string):
            return check_valid_loop(rules, rule, elem), index

        sub_rule = rules[elem]
        if isinstance(sub_rule, str):
            if string[index] == sub_rule:
                index += 1
            else:
                return False, index
        else:
            if isinstance(sub_rule[0], list):
                result = False
                for elem in sub_rule:
                    res, new_index = check_rule(rules, elem, string, index)
                    result = result | res
                    if result:
                        index = new_index
                        break
                if not result:
                    return result, index
            else:
                result, new_index = check_rule(rules, sub_rule, string, index)
                if result:
                    index = new_index
                else:
                    return result, index
    return True, index

# file = open('day19test2.txt', 'r')

file = open('day19input.txt', 'r')

rules = {}
rules_part = True
inputs = []
total = 0
for line in file:
    line = line.strip('\n')
    if not line:
        rules_part = False

    elif rules_part:
        add_and_parse_rule(line, rules)
    else:
        res, index = check_rule(rules, rules['0'], line, 0)
        if res and index == len(line):
            total += 1
file.close()

print(total)
    

