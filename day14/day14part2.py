file = open('day14input.txt')
# file = open('day14testinput.txt')


def find_locs(mem_loc, mask):
    mem_loc_bin = bin(mem_loc).replace('0b', '')

    # pad the strings to be of same length
    length = max(len(mask), len(mem_loc_bin))
    mem_loc_bin = '0' * (length - len(mem_loc_bin)) + mem_loc_bin
    mask = '0' * (length - len(mem_loc_bin)) + mask

    combined = []
    x_marks = []
    for i in range(length):
        if mask[i] == 'X' or mask[i] == '1':
            if mask[i] == 'X':
                x_marks.append(i)
            combined.append(mask[i])
        elif mem_loc_bin[i] == '1':
            combined.append('1')
        else:
            combined.append('0')
    
    combo_power = len(x_marks)
    combos = []
    for num in range(0, 2 ** combo_power):
        combo = bin(num).replace('0b', '')

        # need to pad them to number of x's in mask
        combo = '0' * (combo_power - len(combo)) + combo
        combos.append(combo)
    
    locs = []
    for combo in combos:
        copy = combined[:]
        for i in range(combo_power):
            # sub in the combo numbers for the x's
            copy[ x_marks[i] ] = combo[i]
        locs.append(int(''.join(copy), 2))

    return locs

mem = {}
mask = None

for line in file:
    line = line.strip('\n')
    if 'mask' in line:
        line = line.replace('mask = ', '')
        mask = line.lstrip('0')  # 0's do not make changes
    else:
        line = line.replace('mem[', '').replace(']', '')
        lst = line.split(' = ')
        mem_loc = int(lst[0])
        locs = find_locs(mem_loc, mask)
        for loc in locs:
            mem[loc] = int(lst[1])

file.close()

total = 0
for elem in mem:
    total += mem[elem]

print(total)