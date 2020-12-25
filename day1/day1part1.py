# FILE_NM = 'day1testinput.txt'
FILE_NM = 'day1input.txt'

def main():
    # Print product of two numbers in the file that add up to 2020
    numbers = set()

    file = open(FILE_NM, 'r')

    for line in file:
        number = int(line.strip('\n'))
        if 2020 - number in numbers:
            print(number * (2020 - number))
            break
        numbers.add(number)

    file.close()

main()