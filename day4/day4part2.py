def check_valid(data):
    byr = int(data['byr'])
    if byr < 1920 or byr > 2002:
        return False
    iyr = int(data['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False
    eyr = int(data['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False
    if 'cm' in data['hgt']:
        height = int(data['hgt'].strip('cm'))
        if height < 150 or height > 193:
            return False
    elif 'in' in data['hgt']:
        height = int(data['hgt'].strip('in'))
        if height < 59 or height > 76:
            return False
    else:
        return False
    if data['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    hcl = data['hcl']
    if len(hcl) != 7:
        return False
    if hcl[0] != '#':
        return False
    for char in hcl[1:]:
        # print(hcl[1:])
        if not char.isdigit() and char not in ['a', 'b', 'c', 'd', 'e', 'f']:
            return False

    pid = data['pid']
    if len(pid) != 9:
        return False
    for elem in pid:
        if not elem.isdigit():
            return False
    return True

file = open('day4input.txt', 'r')

valid = 0 
data = {}
for line in file:
    line = line.strip('\n')
    if not line:
        if len(data) == 8 or (len(data) == 7 and 'cid' not in data):
            if check_valid(data):
                valid += 1
        data = {}
    else:
        info_parts = line.split(' ')
        for info in info_parts:
            data[info.split(':')[0]] = info.split(':')[1]

if data:
    if len(data) == 8 or (len(data) == 7 and 'cid' not in data):
        if check_valid(data):
            valid += 1
print(valid)
file.close()
