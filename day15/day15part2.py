# FILE_NM = 'day15testinput.txt'
FILE_NM = 'day15input.txt'
LAST_TURN = 30000000


def read_file(file_nm):
    '''
    Returns:
        curr_num: number to be spoken for the next turn
        spoke_numbers: a dictionary of numbers mapped to the last turn they were said
    '''
    file = open(FILE_NM, 'r')
    prev_num = None
    curr_num = None
    spoken_numbers = {}
    turn = 0

    for line in file:
        line = line.strip('\n').split(',')
        for elem in line:
            if curr_num is None:
                curr_num = int(elem)
            else:
                prev_num = curr_num
                curr_num = int(elem)
                spoken_numbers[prev_num] = turn
            turn += 1

    file.close()
    return curr_num, spoken_numbers

def get_nth_number(curr_num, spoken_numbers_dict, n):
    turn = len(spoken_numbers_dict) + 1

    while turn < n:
        if curr_num not in spoken_numbers_dict:
            spoken_numbers_dict[curr_num] = turn
            curr_num = 0
        else:
            last_turn_spoken = spoken_numbers_dict[curr_num]
            spoken_numbers_dict[curr_num] = turn 
            curr_num = turn - last_turn_spoken

        turn += 1

    return curr_num

def main():
    curr_num, spoken_numbers = read_file(FILE_NM)
    last_num = get_nth_number(curr_num, spoken_numbers, LAST_TURN)
    print(last_num)

main()
