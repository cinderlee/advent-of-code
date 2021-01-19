FILE_TEST_NM = 'day16testinput.txt'
FILE_NM = 'day16input.txt'

def get_valid_numbers(interval_string):
    '''
    Returns a set of valid numbers given an interval in string
    notations.
    '''
    start, end = tuple(int(num) for num in interval_string.split('-'))
    return set(val for val in range(start, end + 1))

def parse_rule(line):
    '''
    Returns a set of valid values for specified rule.
    '''
    field, intervals = line.split(': ')
    interval_one, interval_two = intervals.split(' or ')

    valid_numbers = get_valid_numbers(interval_one)
    valid_numbers.update(get_valid_numbers(interval_two))
    return valid_numbers

def read_file(file_nm):
    '''
    Returns set of valid values for all fields collectively
    and list of nearby tickets. Your ticket is ignored for now.
    '''
    rules_section = True
    your_ticket_section = False
    nearby_tickets_section = False
    valid_numbers = set()
    nearby_tickets = []

    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        if not line:
            continue
        elif 'your ticket' in line:
            your_ticket_section = True
            rules_section = False
        elif 'nearby tickets' in line:
            nearby_tickets_section = True
            your_ticket_section = False
        elif rules_section:
            valid_numbers.update(parse_rule(line))
        elif your_ticket_section:
            continue
        elif nearby_tickets_section:
            # turn line into list of integers
            nearby_tickets.append(tuple(int(num) for num in line.split(',')))
    file.close()

    return valid_numbers, nearby_tickets

def get_invalid_nums(nearby_tickets, valid_set):
    '''
    Returns list of invalid numbers of all the nearby tickets.
    '''
    invalid_numbers = []
    for ticket in nearby_tickets:
        for value in ticket:
            if value not in valid_set:
                invalid_numbers.append(value)
    return invalid_numbers

def solve(file_nm):
    '''
    Returns sum of all invalid values, excluding your ticket.
    '''
    valid_numbers, nearby_tickets = read_file(file_nm)
    return sum(get_invalid_nums(nearby_tickets, valid_numbers))

def main():
    assert(solve(FILE_TEST_NM) == 71)
    print(solve(FILE_NM))

main()
