FILE_NM = 'day4input.txt'
PASSPORT_NUM_FIELDS = 8
BYR_MIN = 1920
BYR_MAX = 2002
IYR_MIN = 2010
IYR_MAX = 2020
EYR_MIN = 2020
EYR_MAX = 2030
HEIGHT_CM_MIN = 150
HEIGHT_CM_MAX = 193
HEIGHT_IN_MIN = 59
HEIGHT_IN_MAX = 76
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
HCL_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f']
HCL_LENGTH = 7
HCL_FIRST_CHAR = '#'

def parse_line(line):
    data = {}
    passport_sections = line.split(' ')
    for section in passport_sections:
        field, val = section.split(':')
        data[field] = val
    return data

def is_valid_byr(byr_data):
    byr = int(byr_data)
    if byr < BYR_MIN or byr > BYR_MAX:
        return False
    return True

def is_valid_iyr(iyr_data):
    iyr = int(iyr_data)
    if iyr < IYR_MIN or iyr > IYR_MAX:
        return False
    return True

def is_valid_eyr(eyr_data):
    eyr = int(eyr_data)
    if eyr < EYR_MIN or eyr > EYR_MAX:
        return False
    return True

def is_valid_height(height_data):
    height = int(height_data.replace('cm', '').replace('in', ''))
    if 'cm' in height_data:
        if height >= HEIGHT_CM_MIN and height <= HEIGHT_CM_MAX:
            return True
    elif 'in' in height_data:
        if height >= HEIGHT_IN_MIN and height <= HEIGHT_IN_MAX:
            return True
    return False

def is_valid_ecl(ecl):
    return ecl in EYE_COLORS

def is_valid_hcl(hcl):
    if len(hcl) != HCL_LENGTH or hcl[0] != HCL_FIRST_CHAR:
        return False
    for index in range(1, len(hcl)):
        char = hcl[index]
        if not char.isdigit() and char not in HCL_LETTERS:
            return False
    return True

def is_valid_pid(pid):
    if len(pid) != 9:
        return False
    for char in pid:
        if not char.isdigit():
            return False
    return True

def can_be_valid(passport_fields_lst):
    if len(passport_fields_lst) == PASSPORT_NUM_FIELDS:
        return True
    elif (len(passport_fields_lst) == PASSPORT_NUM_FIELDS - 1 and
      'cid' not in passport_fields_lst):
        return True
    return False

def is_valid(passport_data):
    return (
        can_be_valid(list(passport_data.keys())) and
        is_valid_byr(passport_data['byr']) and
        is_valid_iyr(passport_data['iyr']) and
        is_valid_eyr(passport_data['eyr']) and
        is_valid_height(passport_data['hgt']) and
        is_valid_ecl(passport_data['ecl']) and
        is_valid_hcl(passport_data['hcl']) and
        is_valid_pid(passport_data['pid'])
    )

def count_valid_passports(file_nm):
    valid = 0
    passport_data = {}
    file = open(file_nm, 'r')

    for line in file:
        line = line.strip('\n')
        if not line:
            if is_valid(passport_data):
                valid += 1
            passport_data = {}
        else:
            passport_data.update(parse_line(line))

    if passport_data and is_valid(passport_data):
        valid += 1

    file.close()
    return valid

def main():
    valid_count = count_valid_passports(FILE_NM)
    print(valid_count)

main()

