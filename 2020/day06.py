# Day 6: Custom Customs

INPUT_FILE_NAME = "./inputs/day06input.txt"
TEST_FILE_NAME = "./inputs/day06testinput.txt"

def read_answers_file(file_nm):
    '''
    Returns a list of group of answers read from a file.
    '''
    file = open(file_nm, 'r')
    groups = file.read().split('\n\n')
    answer_groups = [group.split('\n') for group in groups]
    file.close()
    return answer_groups

def create_answers_log():
    '''
    Returns a dictionary where the key represents the question
    and value represents number of people who answered yes.

    There are 26 yes-or-no questions marked a through z.
    '''
    answers_log = {}
    for i in range(26):
        answers_log[chr(ord('a') + i)] = 0
    return answers_log

def count_unanimous_answers(answers_log, num_group_members):
    '''
    Returns number of answers where everyone in a group answered yes.
    '''
    return list(answers_log.values()).count(num_group_members)

def count_total_answers_part_one(answer_groups):
    '''
    Returns the sum of the sum of questions to which anyone 
    answered yes for each group. 
    '''
    total = 0
    for answer_group in answer_groups:
        answer_set = set()
        for answers in answer_group:
            for answer in answers:
                answer_set.add(answer)
        total += len(answer_set)
    return total

def count_total_answers_part_two(answer_groups):
    '''
    Returns the sum of the sum of questions to which everyone 
    answered yes for each group. 
    '''
    total_answers = 0

    for answer_group in answer_groups:
        answers_log = create_answers_log()
        for answers in answer_group:
            for answer in answers:
                answers_log[answer] += 1
        total_answers += count_unanimous_answers(answers_log, len(answer_group))
    return total_answers

def solve_part_one(answer_groups):
    return count_total_answers_part_one(answer_groups)

def solve_part_two(answer_groups):
    return count_total_answers_part_two(answer_groups)

def main():
    test_answer_groups = read_answers_file(TEST_FILE_NAME)
    assert(solve_part_one(test_answer_groups) == 11)
    assert(solve_part_two(test_answer_groups) == 6)

    answer_groups = read_answers_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(answer_groups))
    print('Part Two:', solve_part_two(answer_groups))

main()