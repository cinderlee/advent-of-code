# file = open('day10testinput.txt')
file = open('day10input.txt')

lst = [0]
for line in file:
    line = line.strip('\n')
    lst.append(int(line))

file.close()

lst.sort()

one_diff = 0
three_diff = 0

for i in range(1, len(lst)):
    diff = lst[i] - lst[i - 1]
    if diff == 1:
        one_diff += 1
    elif diff == 3:
        three_diff += 1

# account for diff between highest element and device volt
three_diff += 1

print(one_diff, three_diff)
print(one_diff * three_diff)
