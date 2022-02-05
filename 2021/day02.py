# Day 2: Dive!

INPUT_FILE_NAME = "./inputs/day02input.txt"
TEST_FILE_NAME = "./inputs/day02testinput.txt"

def parse_file(file_nm):
    '''
    Returns a list of commands for the submarine's planned course
    '''
    commands_lst = []

    file = open(file_nm)
    for line in file:
        command = line.strip('\n').split(" ")
        command[1] = int(command[1])
        commands_lst.append(command)
    file.close()

    return commands_lst

def run_commands(commands_lst):
    '''
    Returns the horizontal position and depth from running a list of commands

    Commands:
        - forward x: increases horizontal position by x
        - down x: increases depth by x
        - up x: decreases depth by x
    '''
    depth = 0
    horizontal_position = 0
    for command in commands_lst:
        direction, value = command

        if direction == 'forward':
            horizontal_position += value
        elif direction == 'up':
            depth -= value
        elif direction == 'down':
            depth += value
    
    return horizontal_position, depth

def run_commands_with_aim(commands_lst):
    '''
    Returns the horizontal position and depth from running a list of commands

    Commands:
        - forward x: 
            - increases horizontal position by x
            - increases depth by aim multiplied by x
        - down x: increases aim by x
        - up x: decreases aim by x
    '''
    aim = 0
    depth = 0
    horizontal_position = 0
    for command in commands_lst:
        direction, value = command

        if direction == 'forward':
            horizontal_position += value
            depth += aim * value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
    
    return horizontal_position, depth

def solve_part_one(commands_lst):
    horizontal_position, depth = run_commands(commands_lst)
    return horizontal_position * depth

def solve_part_two(commands_lst):
    horizontal_position, depth = run_commands_with_aim(commands_lst)
    return horizontal_position * depth

def main():
    test_commands_lst = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_commands_lst) == 150)
    assert(solve_part_two(test_commands_lst) == 900)

    commands_lst = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(commands_lst))
    print('Part Two:', solve_part_two(commands_lst))

main()
