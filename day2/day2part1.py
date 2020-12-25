# FILE_NM = 'day2testinput.txt'
FILE_NM = 'day2input.txt'

def parse_line(line):
    occurence_info, letter, password = line.strip('\n').replace(':', '').split(' ')
    min_num, max_num = occurence_info.split('-') 
    return int(min_num), int(max_num), letter, password

def check_valid_password(password_rule_info):
    min_occurence, max_occurence, letter, password = password_rule_info
    count = 0

    for character in password:
        if character == letter:
            count += 1
        if count > max_occurence:
            break
    
    return count >= min_occurence and count <= max_occurence

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
    print(get_valid_password_count(FILE_NM))

main()