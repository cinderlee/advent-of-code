# Day 4: The Treachery of Whales

import math 

INPUT_FILE_NAME = "./inputs/day7input.txt"
TEST_FILE_NAME = "./inputs/day7testinput.txt"

def parse_file(file_nm):
    file = open(file_nm, 'r')

    crab_positions = file.readline().strip('\n').split(',')
    for i in range(len(crab_positions)):
        crab_positions[i] = int(crab_positions[i])

    file.close()
    return crab_positions

def find_least_fuel_cost_part_one(crab_positions):
    '''
    Return the least fuel possible to align the crabs to have the 
    same horizontal position.

    Crab submarine engines burn 1 unit of fuel for each step.
    '''
    minimum = min(crab_positions)
    maximum = max(crab_positions)

    steps = []
    for horizontal_posiiton in range(minimum, maximum):
        cost = 0
        for elem in crab_positions:
            cost += abs(elem - horizontal_posiiton)
        
        steps.append(cost)
    return min(steps)

def find_least_fuel_cost_part_two(crab_positions):
    '''
    Return the least fuel possible to align the crabs to have the 
    same horizontal position.

    Crab submarine engines burn 1 more unit of fuel for each step
    than the previous step. 
    '''
    minimum = min(crab_positions)
    maximum = max(crab_positions)

    steps = []
    for i in range(minimum, maximum):
        cost = 0
        for elem in crab_positions:
            total_steps_count = abs(elem - i)
            # sum of arithmetic sequence
            cost += int(total_steps_count * (1 + total_steps_count) / 2)
        
        steps.append(cost)
    return min(steps)

def solve_part_one(crab_positions):
    return find_least_fuel_cost_part_one(crab_positions)

def solve_part_two(crab_positions):
    return find_least_fuel_cost_part_two(crab_positions)

def main():
    test_crab_positions = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_crab_positions) == 37)
    assert(solve_part_two(test_crab_positions) == 168)

    crab_positions = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(crab_positions))
    print('Part Two:', solve_part_two(crab_positions))

main()