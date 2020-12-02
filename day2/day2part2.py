# Day 2

valid_pw = 0

file = open("day2testinput.txt", 'r')

for line in file:
    data = line.strip('\n').split(' ')
    numbers = data[0].split('-')
    index_one = int(numbers[0]) - 1 # to make the first character start at index 0 
    index_two = int(numbers[1]) - 1
    letter = data[1].strip(':')
    pw = data[-1]

    if index_two >= len(pw):
        continue

    if pw[index_one] == letter and pw[index_two] == letter:
        continue
    
    elif pw[index_one] == letter:
        valid_pw += 1

    elif pw[index_two] == letter:
        valid_pw += 1

file.close()

print(valid_pw)