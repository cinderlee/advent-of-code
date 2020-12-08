file = open('day8input.txt')

instr = []
acc = 0
for line in file:
    parts = line.strip('\n').split(' ')
    instr.append([parts[0], int(parts[1])])

file.close()

pointer = 0
locs = set()

while pointer not in locs and pointer >= 0 and pointer < len(instr):
    locs.add(pointer)
    ins, num = instr[pointer]

    if ins == 'nop':
        pointer += 1
    elif ins == 'acc':
        acc += num
        pointer += 1
    else:
        pointer = pointer + num

print(acc)