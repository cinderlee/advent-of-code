# Day 1
file = open('day1input.txt', 'r')

lst = file.read().split('\n')
for index in range(len(lst)):
    lst[index] = int(lst[index])

for index in range(len(lst)):
    first_num = lst[index]
    next_diff = 2020 - first_num

    for index2 in range(index + 1, len(lst)):
        if next_diff - lst[index2] in lst:
            print(first_num * lst[index2] * (next_diff - lst[index2]))
            break

file.close()