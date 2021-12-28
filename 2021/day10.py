# Day 10: Syntax Scoring

INPUT_FILE_NAME = "./inputs/day10input.txt"
TEST_FILE_NAME = "./inputs/day10testinput.txt"

CHUNK_ERROR_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

CHUNK_MATCH = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

COMPLETE_CHUNK_SCORE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def parse_file(file_nm):
    '''
    Returns a list of the navigation subsystem lines, each 
    line containing a series of chunks.
    '''
    file = open(file_nm, 'r')
    navigation_subsystem_lines = file.read().split('\n')
    file.close()
    return navigation_subsystem_lines

def evaluate_syntax_error_score(line):
    '''
    Returns the syntax error score of a line. The syntax error 
    score is the score of the first illegal character in the line. 
    
    Returns 0 if the line is not corrupted (incomplete lines).
    '''
    chunk_stack = []
    for chunk in line:
        if chunk in '({[<':
            chunk_stack.append(chunk)
        else:
            if chunk_stack[-1] != CHUNK_MATCH[chunk]:
                return CHUNK_ERROR_POINTS[chunk]
            else:
                chunk_stack.pop()
    return 0

def evaluate_completion_score(line):
    '''
    Returns the completion score of a line. The completion score is 
    calculated by:
    - Start with a score of 0 
    - For each character that completes a chunk, multiple the score by 5
      and add the score of the character.

    Returns 0 if the line is corrupted. 
    '''
    chunk_stack = []
    for chunk in line:
        if chunk in '({[<':
            chunk_stack.append(chunk)
        else:
            if chunk_stack[-1] != CHUNK_MATCH[chunk]:
                # corrupted
                return 0
            else:
                chunk_stack.pop()

    score = 0
    for i in range(len(chunk_stack) - 1, -1, -1):
        chunk = chunk_stack[i]
        score = score * 5 + COMPLETE_CHUNK_SCORE[chunk]
    return score

def solve_part_one(navigation_subsystem_lines):
    '''
    Returns the total score of all the corrupted lines 
    in the navigation subsystem.
    '''
    total_syntax_error_score = 0
    for line in navigation_subsystem_lines:
        total_syntax_error_score += evaluate_syntax_error_score(line)

    return total_syntax_error_score

def solve_part_two(navigation_subsystem_lines):
    '''
    Returns the median of the completion scores for 
    all incompleted lines in the navigation subsystem.
    '''
    completion_scores = []
    for line in navigation_subsystem_lines:
        score = evaluate_completion_score(line)
        if score != 0:
            completion_scores.append(score)

    completion_scores.sort()
    return completion_scores[len(completion_scores) // 2]

def main():
    test_navigation_subsystem_lines = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_navigation_subsystem_lines) == 26397)
    assert(solve_part_two(test_navigation_subsystem_lines) == 288957)

    navigation_subsystem_lines = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(navigation_subsystem_lines))
    print('Part Two:', solve_part_two(navigation_subsystem_lines))

main()