# Day 2: Password Philosophy

INPUT_FILE_NAME = "./inputs/day02input.txt"
TEST_FILE_NAME = "./inputs/day02testinput.txt"

def parse_line(line):
    '''
    Each line in a file represents a password policy, where it states
    the rule how a given letter must appear in a valid password.

    For part one, the rule specifies the minimum and maximum amount of times
    the letter can appear in the password.

    For part two, the rule specifies the first and second position a letter 
    must appear at (cannot appear at both positions).

    Returns:
        first number of the rule,
        second number of the rule,
        the letter for the specified policy,
        the password
    '''
    policy_numbers, letter, password = line.strip('\n').replace(':', '').split(' ')
    policy_number_one, policy_number_two = policy_numbers.split('-') 
    return int(policy_number_one), int(policy_number_two), letter, password

def read_file(file_nm):
    '''
    Returns a list of tuples representing the password policies in a file.
    '''
    password_policies = []
    file = open(file_nm, 'r')
    for line in file:
        password_policies.append(parse_line(line))
    file.close()
    return password_policies

def check_valid_password_part_one(password_rule_info):
    ''' 
    Checks if a password is valid given the password rule. The password rule
    contains the minimum and maximum times a letter can appear in the password.
    '''
    min_occurence, max_occurence, letter, password = password_rule_info
    count = 0

    for character in password:
        if character == letter:
            count += 1
        if count > max_occurence:
            break
    
    return count >= min_occurence and count <= max_occurence

def check_valid_password_part_two(password_rule_info):
    ''' 
    Checks if a password is valid given the password rule. The password rule
    contains the two locations that a letter can appear in the password.
    The letter can only appear at one of the two locations.
    '''
    pos_one, pos_two, letter, password = password_rule_info
    # offset positions to start at index 0
    pos_one -= 1
    pos_two -= 1
    
    if pos_two >= len(password):
        return False

    check_pos_one = password[pos_one] == letter
    check_pos_two = password[pos_two] == letter
    
    # Only one of the two positions can be the letter
    return check_pos_one ^ check_pos_two

def get_valid_password_count(password_policies, is_valid_password):
    '''
    Returns number of valid passwords given a list of password policies
    and a method to validate a password
    '''
    valid_pw_count = 0

    for policy in password_policies:
        if is_valid_password(policy):
           valid_pw_count += 1

    return valid_pw_count

def solve_part_one(password_policies):
    return get_valid_password_count(password_policies, check_valid_password_part_one)

def solve_part_two(password_policies):
    return get_valid_password_count(password_policies, check_valid_password_part_two)

def main():
    test_password_policies = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_password_policies) == 2)
    assert(solve_part_two(test_password_policies) == 1)

    password_policies = read_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(password_policies))
    print('Part Two:', solve_part_two(password_policies))

main()
