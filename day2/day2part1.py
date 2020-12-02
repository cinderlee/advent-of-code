# Day 2

valid_pw = 0

file = open("day2input.txt", 'r')

for line in file:
    data = line.strip('\n').split(' ')
    numbers = data[0].split('-')
    minimum = int(numbers[0])
    maximum = int(numbers[1])
    letter = data[1].strip(':')

    count = 0

    for let in data[-1]: 
        if let == letter:
            count += 1
        if count > maximum:
            break

    if count >= minimum and count <= maximum:
        valid_pw += 1

file.close()

print(valid_pw)