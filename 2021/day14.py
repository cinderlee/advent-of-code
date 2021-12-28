# Day 14: Extended Polymerization

INPUT_FILE_NAME = "./inputs/day14input.txt"
TEST_FILE_NAME = "./inputs/day14testinput.txt"

def parse_file(file_nm):
    '''
    Returns the polymer template and list of pair insertion rules in
    the form of a dictionary. 

    Dictionary:
        - key: pair rule applies to
        - value: element to insert between the pair
    '''
    file = open(file_nm, 'r')
    polymer_template = file.readline().strip('\n')
    
    file.readline()     # empty line

    insertion_rules = {}
    for line in file:
        insertion_rule_parts = line.strip('\n').split(' -> ')
        insertion_rules[insertion_rule_parts[0]] = insertion_rule_parts[1]

    file.close()
    
    return polymer_template, insertion_rules

def count_elements(polymer_template):
    '''
    Returns a dictionary mapping an element to the number of times it appears
    in the polymer template
    '''
    element_count = {}
    for element in polymer_template:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

def count_pairs(polymer_template, insertion_rules_keys):
    '''
    Returns a dictionary mapping the pairs in the insertion rules to the number
    of times they appear in the polymer template
    '''
    pair_count = {}
    for i in range(len(polymer_template) - 1):
        pair = polymer_template[i : i + 2]
        if pair not in insertion_rules_keys:
            continue
        if pair in pair_count:
            pair_count[pair] += 1
        else:
            pair_count[pair] = 1
    return pair_count

def polymerize(polymer_template, insertion_rules, times):
    '''
    Polymerizes a template given a set of insertion rules to find
    an optimal polymer formula to reinforce the submarine. Returns
    the difference between the quantity of the most common element and
    the least common element in the final polymer.

    For each rule, if the given pair exists in the template, insert the
    mapped element in between the pair.
        Ex: For the rule AB -> C, the resulting sub-polymer would be ABC
    '''
    element_count = count_elements(polymer_template)
    pair_count = count_pairs(polymer_template, insertion_rules.keys())
    
    for _ in range(times):
        next_pair_count = {}
        for pair, count in pair_count.items():
            replacement = insertion_rules[pair]
            if replacement in element_count:
                element_count[replacement] += count
            else:
                element_count[replacement] = count

            next_pair_one = pair[0] + replacement
            next_pair_two = replacement + pair[1]
            
            if next_pair_one in next_pair_count:
                next_pair_count[next_pair_one] += count
            else:
                next_pair_count[next_pair_one] = count

            if next_pair_two in next_pair_count:
                next_pair_count[next_pair_two] += count
            else:
                next_pair_count[next_pair_two] = count

        pair_count = next_pair_count
    counts = element_count.values()
    return max(counts) - min(counts)

def solve_part_one(polymer_template, insertion_rules):
    return polymerize(polymer_template, insertion_rules, 10)

def solve_part_two(polymer_template, insertion_rules):
    return polymerize(polymer_template, insertion_rules, 40)

def main():
    polymer_template_test, insertion_rules_test = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(polymer_template_test, insertion_rules_test) == 1588)
    assert(solve_part_two(polymer_template_test, insertion_rules_test) == 2188189693529)

    polymer_template, insertion_rules = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(polymer_template, insertion_rules))
    print('Part Two:', solve_part_two(polymer_template, insertion_rules))

main()
