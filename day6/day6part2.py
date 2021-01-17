FILE_TEST_NM = 'day6testinput.txt'
FILE_NM = 'day6input.txt'

def create_answers_log():
    '''
    Returns a dictionary where the key represents the question
    and value represents number of people who answered yes.

    There are 26 yes-or-o questions marked a through z.
    '''
    answers_log = {}
    for i in range(26):
        answers_log[chr(ord('a') + i)] = 0
    return answers_log

def count_unanimous_answers(answers_log, num_group_members):
    '''
    Returns number of answers where everyone in a group answered yes
    Resets the answers_log for the next group count.
    '''
    total = 0
    for answer in answers_log:
        if answers_log[answer] == num_group_members:
            total += 1
        answers_log[answer] = 0
    return total

def count_total_answers(file_nm):
    '''
    Returns the sum of the sum of questions to which everyone 
    answered yes for each group. 
    '''
    file = open(file_nm, 'r')
    answers_log = create_answers_log()
    total_answers = 0
    members_count = 0

    for line in file:
        line = line.strip('\n')
        if not line:
            total_answers += count_unanimous_answers(answers_log, members_count)
            members_count = 0
        else:
            for ans in line:
                answers_log[ans] += 1
            members_count += 1

    file.close()

    # last group also needs to be accounted for!
    total_answers += count_unanimous_answers(answers_log, members_count)
    return total_answers

def main():
    assert(count_total_answers(FILE_TEST_NM) == 6)
    print(count_total_answers(FILE_NM))

main()