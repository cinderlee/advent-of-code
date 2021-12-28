# Day 3: Binary Diagnostic

INPUT_FILE_NAME = "./inputs/day3input.txt"
TEST_FILE_NAME = "./inputs/day3testinput.txt"

def parse_file(file_nm):
    '''
    Returns a list of binary numbers representing the 
    submarine's diagnostic report.
    '''

    diagnostic_report = []

    file = open(file_nm)
    for line in file:
        diagnostic_report.append(line.strip('\n'))

    file.close()

    return diagnostic_report

def evaluate_power_consumption(diagnostic_report):
    '''
    Returns the submarine's power consumption given the diagnostic report.

    Power consumption is calculated by multiplying gamma rate by the epsilon rate. 
    Each bit of the gamma rate is the most common bit in the matching position
    of each binary number. Each bit of the epsilon rate is the least common bit.
    '''

    gamma_bits = []
    epsilon_bits = []

    for i in range(len(diagnostic_report[0])):
        ones_bits_counter = 0
        for binary_num in diagnostic_report:
            if binary_num[i] == '1':
                ones_bits_counter += 1
        
        if ones_bits_counter > len(diagnostic_report) // 2:
            gamma_bits.append('1')
            epsilon_bits.append('0')
        else:
            gamma_bits.append('0')
            epsilon_bits.append('1')

    gamma_rate = int(''.join(gamma_bits), 2)
    epsilon_rate = int(''.join(epsilon_bits), 2)
    return gamma_rate * epsilon_rate

def evaluate_oxygen_generator_rating(diagnostic_report):
    '''
    Returns the oxygen generator rating of the submarine.

    Starting from the first bit, keep/discard numbers that match/do not match
    the bit criteria. Repeat this process for every bit until one number remains

    Bit criteria:
        - Find the most common bit in the corresponding posiiton. 
        - Keep numbers with the most common bit
        - Keep numbers with value 1 in the bit position if there is a tie
    '''

    end_index = len(diagnostic_report) - 1

    for i in range(len(diagnostic_report[0])):
        count_ones_bits = 0
        count_zeroes_bits = 0
        for index in range(end_index + 1):
            if diagnostic_report[index][i] == '1':
                count_ones_bits += 1
            else:
                count_zeroes_bits += 1
        
        curr_index = 0

        # Shift matching numbers to the front
        while curr_index <= end_index:
            if count_ones_bits >= count_zeroes_bits and diagnostic_report[curr_index][i] == '1':
                curr_index += 1
            elif count_zeroes_bits > count_ones_bits and diagnostic_report[curr_index][i] == '0':
                curr_index += 1
            else:
                diagnostic_report[curr_index], diagnostic_report[end_index] = diagnostic_report[end_index], diagnostic_report[curr_index]
                end_index -= 1
    
        if end_index == 0:
            break

    return int(diagnostic_report[0], 2)

def evaluate_co2_scrubber_rating(diagnostic_report):
    '''
    Returns the CO2 scrubber rating of the submarine.

    Starting from the first bit, keep/discard numbers that match/do not match
    the bit criteria. Repeat this process for every bit until one number remains

    Bit criteria:
        - Find the least common bit in the corresponding posiiton. 
        - Keep numbers with the least common bit
        - Keep numbers with value 0 in the bit position if there is a tie
    '''
    
    end_index = len(diagnostic_report) - 1

    for i in range(len(diagnostic_report[0])):
        count_ones_bits = 0
        count_zeroes_bits = 0
        for index in range(end_index + 1):
            if diagnostic_report[index][i] == '1':
                count_ones_bits += 1
            else:
                count_zeroes_bits += 1
        
        curr_index = 0

        # Shift matching numbers to the front
        while curr_index <= end_index:
            if count_zeroes_bits <= count_ones_bits and diagnostic_report[curr_index][i] == '0':
                curr_index += 1
            elif count_ones_bits < count_zeroes_bits and diagnostic_report[curr_index][i] == '1':
                curr_index += 1
            else:
                diagnostic_report[curr_index], diagnostic_report[end_index] = diagnostic_report[end_index], diagnostic_report[curr_index]
                end_index -= 1
    
        if end_index == 0:
            break

    return int(diagnostic_report[0], 2)

def evaluate_life_support_rating(diagnostic_report):
    '''
    Returns the submarine's life support rating given the diagnostic report.

    Life support rating is calculated by multiplying the oxygen generator
    rating and CO2 scrubber rating.
    '''

    return evaluate_oxygen_generator_rating(diagnostic_report) * evaluate_co2_scrubber_rating(diagnostic_report)

def solve_part_one(diagnostic_report):
    return evaluate_power_consumption(diagnostic_report)

def solve_part_two(diagnostic_report):
    return evaluate_life_support_rating(diagnostic_report)

def main():
    test_diagnostic_report = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_diagnostic_report) == 198)
    assert(solve_part_two(test_diagnostic_report) == 230)

    diagnostic_report = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(diagnostic_report))
    print('Part Two:', solve_part_two(diagnostic_report))

main()
