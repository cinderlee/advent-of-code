FILE_TEST_NM = 'day2testinput.txt'
FILE_NM = 'day2input.txt'

def parse_line(line):
    position_info, letter, password = line.strip('\n').replace(':', '').split(' ')
    pos_one, pos_two = position_info.split('-') 
    # Offset positions to start at index 0
    return int(pos_one) - 1, int(pos_two) - 1, letter, password

def check_valid_password(password_rule_info):
    pos_one, pos_two, letter, password = password_rule_info
    
    if pos_two >= len(password):
        return False

    check_pos_one = password[pos_one] == letter
    check_pos_two = password[pos_two] == letter
    
    # Only one of the two positions can be the letter
    return check_pos_one ^ check_pos_two

def get_valid_password_count(file_nm):
    valid_pw_count = 0
    file = open(file_nm, 'r')

    for line in file:
        password_rule_info = parse_line(line)
        if check_valid_password(password_rule_info):
           valid_pw_count += 1

    file.close()
    return valid_pw_count

def main():
    assert(get_valid_password_count(FILE_TEST_NM) == 1)
    print(get_valid_password_count(FILE_NM))

main()
