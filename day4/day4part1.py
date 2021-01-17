FILE_TEST_NM = 'day4testinput.txt'
FILE_NM = 'day4input.txt'
PASSPORT_NUM_FIELDS = 8


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

def parse_line(line):
    '''
    Returns a dictionary of fields and values specified for a passport.
    Note: A passport can be represented by several file lines, so this 
    really returns a sub-dictionary of the passport data.
    '''
    fields = []
    passport_sections = line.split(' ')
    for section in passport_sections:
        fields.append(section.split(':')[0])

    return fields

def count_valid_passports(file_nm):
    '''
    Returns number of valid passports from a file.
    '''
    valid = 0
    passport_fields = []
    file = open(file_nm, 'r')

    for line in file:
        line = line.strip('\n')
        if not line:
            if can_be_valid(passport_fields):
                valid += 1
            passport_fields = []
        else:
            passport_fields.extend(parse_line(line))

    if passport_fields and can_be_valid(passport_fields):
        valid += 1

    file.close()
    return valid

def main():
    assert(count_valid_passports(FILE_TEST_NM) == 2)
    print(count_valid_passports(FILE_NM))

main()