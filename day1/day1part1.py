# Day 1
file = open('day1input.txt', 'r')

lst = file.read().split('\n')
for index in range(len(lst)):
    lst[index] = int(lst[index])

for elem in lst:
    if 2020 - elem in lst:
        print(elem, 2020-elem)
        print(elem * (2020 - elem))
        break

file.close()