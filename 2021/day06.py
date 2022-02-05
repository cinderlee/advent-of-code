# Day 6: Lanternfish

INPUT_FILE_NAME = "./inputs/day06input.txt"
TEST_FILE_NAME = "./inputs/day06testinput.txt"

def parse_file(file_nm):
    '''
    Returns a list of counts of lanterfish based on the internal timer,
    which is the amount of days it has until it creates another lanternfish.

    Example: index 1 in the list stores the count of lanternfish that have
    1 day left until it creates another lanternfish.
    '''
    lanternfish = [0 for _ in range(9)]
    file = open(file_nm, 'r')
    lanternfish_input = file.readline().strip('\n').split(',')
    for fish in lanternfish_input:
        lanternfish[int(fish)] += 1
    file.close()

    return lanternfish

def simulate_spawn_lanternfish(lanternfish, num_days):
    '''
    Returns the number of lanternfish after x number of days. Internal timer
    decreases by 1 after each day. Lanternfish whose internal timer is 0 create
    a new lanternfish with internal timer of 8 and have their timers reset to 6. 
    '''
    for _ in range(num_days):
        lanternfish_parents = lanternfish[0]
        for i in range(8):
            lanternfish[i] = lanternfish[i + 1]
        lanternfish[6] += lanternfish_parents
        lanternfish[8] = lanternfish_parents
    return sum(lanternfish)

def solve_part_one(lanternfish):
    return simulate_spawn_lanternfish(lanternfish, 80)

def solve_part_two(lanternfish):
    return simulate_spawn_lanternfish(lanternfish, 256)

def main():
    test_lanternfish = parse_file(TEST_FILE_NAME)
    test_lanternfish_copy = test_lanternfish[:]
    assert(solve_part_one(test_lanternfish) == 5934)
    assert(solve_part_two(test_lanternfish_copy) == 26984457539)

    lanternfish = parse_file(INPUT_FILE_NAME)
    lanternfish_copy = lanternfish[:]
    print('Part One:', solve_part_one(lanternfish))
    print('Part Two:', solve_part_two(lanternfish_copy))

main()