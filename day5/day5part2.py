def find_row(data):
    start = 0
    end = 127
    for elem in data:
        # print(start, end)
        num_rows = end - start + 1
        half = num_rows // 2
        if elem == 'F':
            end -= half
        else:
            start += half

    return start

def find_col(data):
    # print(dat/a)
    start = 0
    end = 7
    for elem in data:
        # print(start, end)
        num_cols = end - start + 1
        half = num_cols // 2
        if elem == 'L':
            end -= half
        else:
            start += half

    return start

def find_seat(data):
    row = find_row(data[:7])
    col = find_col(data[7:])

    # print (row, col)
    return row * 8 + col

file = open('day5input.txt', 'r')
max = 0

lst = []

for line in file:
    txt = line.strip('\n')
    res = find_seat(txt)
    if res > max:
        max = res
    lst.append(res)

file.close()

# print (find_seat('BFFFBBFRRR'))
# print (find_seat('FFFBBBFRRR'))
# print (find_seat('BBFFBBFRLL'))
# print (find_seat('FBFBBFFRLR'))

min = min(lst)

for i in range(min, max):
    if i not in lst:
        print(i)

print(lst)
print(526 in lst)
print(528 in lst)