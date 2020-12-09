file = open('day9input.txt')

numbers = []
preamble = 25
for line in file:
    line = line.strip('\n')
    numbers.append(int(line))

file.close()

pointer = 25

while pointer < len(numbers):
    sub_lst = numbers[pointer - preamble:pointer]
    total = numbers[pointer]
    outlier = True
    for elem in sub_lst:
        if total - elem in sub_lst:
            outlier = False
            break
        else:
            continue

    if outlier:
        print(total)
        break
    
    pointer += 1