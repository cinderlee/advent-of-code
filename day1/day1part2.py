FILE_TEST_NM = 'day1testinput.txt'
FILE_NM = 'day1input.txt'

def read_file(file_nm):
    # Return a list of ints read from a file

    file = open(file_nm, 'r')
    lst = file.read().split('\n')
    file.close()

    for index in range(len(lst)):
        lst[index] = int(lst[index])

    return lst

def get_three_nums(lst):
    # Find three numbers that add up to 2020

    for index in range(len(lst)):
        first_num = lst[index]
        sub_sum = 2020 - first_num

        for index2 in range(index + 1, len(lst)):
            if sub_sum - lst[index2] in lst:
                return first_num, lst[index2], sub_sum - lst[index2]

def solve(file_nm):
    nums_lst = read_file(file_nm)
    num_one, num_two, num_three = get_three_nums(nums_lst)
    return num_one * num_two * num_three

def main():
    assert(solve(FILE_TEST_NM) == 241861950)
    print(solve(FILE_NM))

main()