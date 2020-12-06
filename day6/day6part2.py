file = open('day6input.txt')

sum_total = 0

answer_key = {}
for i in range(0, 26):
    answer_key[chr(ord('a') + i)] = 0

group_count = 0

for line in file:
    line = line.strip('\n')
    
    if not line:
        for key in answer_key:
            if answer_key[key] == group_count:
                sum_total += 1
            answer_key[key] = 0
        group_count = 0
    else:
        for elem in line:
            answer_key[elem] += 1
        group_count += 1

if group_count != 0:
    for key in answer_key:
        if answer_key[key] == group_count:
            sum_total += 1

print(sum_total)