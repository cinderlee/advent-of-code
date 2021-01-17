FILE_TEST_NM = 'day1testinput.txt'
FILE_NM = 'day1input.txt'

def solve(file_nm):
    '''
    Returns product of two numbers in the file that add up to 2020
    '''
    numbers = set()

    file = open(file_nm, 'r')

    for line in file:
        number = int(line.strip('\n'))
        if 2020 - number in numbers:
            return(number * (2020 - number))
            break
        numbers.add(number)

    file.close()

def main():
    assert(solve(FILE_TEST_NM) == 514579)
    print(solve(FILE_NM))

main()