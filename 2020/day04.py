# Day 4: Passport Processing

INPUT_FILE_NAME = "./inputs/day4input.txt"
TEST_FILE_NAME = "./inputs/day4testinput.txt"

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
    '''
    Returns a dictionary of fields and values specified for a passport.
    Note: A passport can be represented by several file lines, so this 
    really returns a sub-dictionary of the passport data.
    '''
    data = {}
    passport_sections = line.split(' ')
    for section in passport_sections:
        field, val = section.split(':')
        data[field] = val
    return data

def read_passports_file(file_nm):
    '''
    Returns a list of passports, each represented as a dictionary of passport
    fields mapped to their values.
    '''
    passports_lst = []
    file = open(file_nm, 'r')
    passports = file.read().split('\n\n')
    for passport in passports:
        passport_info = {}
        passport_parts = passport.split('\n')
        for part in passport_parts:
            passport_info.update(parse_line(part))
        passports_lst.append(passport_info)

    file.close()
    return passports_lst

def is_valid_byr(byr_data):
    '''
    Returns whether birth year is valid (at least 1920 and at most 2002)
    '''
    byr = int(byr_data)
    if byr < BYR_MIN or byr > BYR_MAX:
        return False
    return True

def is_valid_iyr(iyr_data):
    '''
    Returns whether issue year is valid (at least 2010 and at most 2020)
    '''
    iyr = int(iyr_data)
    if iyr < IYR_MIN or iyr > IYR_MAX:
        return False
    return True

def is_valid_eyr(eyr_data):
    '''
    Returns whether expiration year is valid (at least 2020 and at most 2030)
    '''
    eyr = int(eyr_data)
    if eyr < EYR_MIN or eyr > EYR_MAX:
        return False
    return True

def is_valid_height(height_data):
    '''
    Returns whether height is valid.

    Valid units: cm, in
    Valid range:
        - cm: at least 150, at most 193
        - in: at least 59, at most 75
    '''
    height = int(height_data.replace('cm', '').replace('in', ''))
    if 'cm' in height_data:
        if height >= HEIGHT_CM_MIN and height <= HEIGHT_CM_MAX:
            return True
    elif 'in' in height_data:
        if height >= HEIGHT_IN_MIN and height <= HEIGHT_IN_MAX:
            return True
    return False

def is_valid_ecl(ecl):
    '''
    Returns whether eye color is valid. Must be one of:
    amb, blu, brn, gry, grn, hzl, oth
    '''
    return ecl in EYE_COLORS

def is_valid_hcl(hcl):
    '''
    Returns whether hair color is valid. 
    Format: starts with #, followed by 6 characters containing 0-9 or a-f
    '''
    if len(hcl) != HCL_LENGTH or hcl[0] != HCL_FIRST_CHAR:
        return False
    for index in range(1, len(hcl)):
        char = hcl[index]
        if not char.isdigit() and char not in HCL_LETTERS:
            return False
    return True

def is_valid_pid(pid):
    '''
    Returns whether passport id is valid: contains 9 numbers including 
    leading zeroes.
    '''
    if len(pid) != 9:
        return False
    for char in pid:
        if not char.isdigit():
            return False
    return True

def can_be_valid(passport_fields_lst):
    '''
    A valid passport has eight fields present for:
        Birth Year, Issue Year, Expiration Year, Height,
        Hair Color, Eye Color, Passport ID, Country ID
    If Country ID is missing, a passport is still considered to be valid.

    Returns whether a passport is valid given a list of fields specified.
    '''
    if len(passport_fields_lst) == PASSPORT_NUM_FIELDS:
        return True
    elif (len(passport_fields_lst) == PASSPORT_NUM_FIELDS - 1 and
      'cid' not in passport_fields_lst):
        return True
    return False

def is_valid(passport_data):
    '''
    Returns whether a passport is valid
    '''
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

def solve_part_one(passports):
    '''
    Returns the number of passports that contain all the required fields.
    '''
    valid_passports = 0
    for passport in passports:
        if can_be_valid(list(passport.keys())):
            valid_passports += 1
    return valid_passports

def solve_part_two(passports):
    '''
    Returns the number of passports that contain all the required fields
    and valid values for those fields.
    '''
    valid_passports = 0
    for passport in passports:
        if is_valid(passport):
            valid_passports += 1
    return valid_passports

def main():
    test_passports = read_passports_file(TEST_FILE_NAME)
    assert(solve_part_one(test_passports) == 2)

    passports = read_passports_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(passports))
    print('Part Two:', solve_part_two(passports))

main()

