MAX_NUM = 1000000
NUM_MOVES = 10000000

TEST_INPUT = '389125467'
INPUT = '315679824'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, input_string):
        '''
        Creates a cyclic linked list given an input string of numbers representing 
        cup labels. The cups are arranged in a circle clockwise.

        Member variables:
            cups: dictionary where keys are the cup labels and values are the cup nodes
            max_cup_number: maximum cup number label
        '''
        self.cups = {}
        self.max_cup_number = 0

        prev = None
        for elem in input_string:
            cup_number = int(elem)
            node = Node(cup_number)
            self.cups[cup_number] = node
            if prev:
                self.cups[prev].next = node
            prev = cup_number
            self.max_cup_number = max(self.max_cup_number, cup_number)

        self.cups[prev].next = self.cups[int(input_string[0])]


    def get_cup(self, num):
        '''
        Returns the node paired to a given number
        '''
        return self.cups[num]

    def get_max(self):
        '''
        Returns the maximum cup number
        '''
        return self.max_cup_number

    def get_post_order(self, num):
        '''
        Returns a string of numbers representing the order of cup positions
        after the cup labeled num.
        '''
        lst = []
        curr_cup = self.get_cup(num).next

        while curr_cup.data != num:
            lst.append(str(curr_cup.data))
            curr_cup = curr_cup.next

        return ''.join(lst)

    def get_stars(self):
        '''
        The crab hid stars under two cups that are immediately clockwise of cup 1.
        Returns the cup numbers where the stars are hidden under.
        '''
        first_star = self.get_cup(1).next
        second_star = first_star.next

        return first_star.data, second_star.data

def generate_input_list(input_txt):
    '''
    In the Crab Game, the crab arranges one million cups. THe labeling in the 
    input text is correct but the remaining cups are numbered starting from the
    maximum number in the list up until one million. 
    
    Returns a list of numbers representing the cup labels in clockwise order.
    '''
    input_lst = [int(elem) for elem in input_txt]
    max_cup_label = max(input_lst)
    for elem in range(max_cup_label + 1, MAX_NUM + 1):
        input_lst.append(elem)

    return input_lst

def play_crab_game(linked_lst, start_cup, num_moves):
    '''
    For each move, the crab will:
        1. Pick up and remove 3 cups that are immediately clockwise of the current cup
        2. Select a destination cup that has a label equal to 1 less than the current cup's
           label. If a cup that was picked up is selected, the crab will keep 
           subtracting until it finds a cup that wasn't picked up. If the value falls below
           the minimum cup label, it wraps around to the highest cup label.
        3. Places the 3 cups that were picked up immediately clockwise to the destination
           cup, maintaining the same order as they were picked up. 
        4. Select a new current cup, immediately clockwise to the current cup.
    '''
    max_cup_label = linked_lst.get_max()
    curr_cup = linked_lst.get_cup(start_cup)
    count = 0

    while count < num_moves:
        first_cup = curr_cup.next
        second_cup = first_cup.next
        third_cup = second_cup.next
        curr_cup.next = third_cup.next

        three_cups_data = [first_cup.data, second_cup.data, third_cup.data]
        dest_cup = curr_cup.data 

        while True:
            dest_cup -= 1
            if dest_cup == 0:
                dest_cup = max_cup_label
            if dest_cup in three_cups_data:
                continue
            else:
                dest_node = linked_lst.get_cup(dest_cup)
                dest_cup_next = dest_node.next
                dest_node.next = first_cup
                third_cup.next = dest_cup_next
                break

        count += 1
        curr_cup = curr_cup.next

def solve(input_txt, num_moves):
    '''
    A crab wants to play a game with 1 million cups ordered clockwise in the input text.
    The first number in the input is the current cup and the crab is going to 
    perform a number of moves. The crab also hide stars under two cups immediately
    clockwise from cup 1.

    Returns the product of the cup labels where the crab hid stars under. 
    '''
    input_lst = generate_input_list(input_txt)
    linked_lst = LinkedList(input_lst)
    start_cup = int(input_txt[0])
    play_crab_game(linked_lst, start_cup, num_moves)

    first_star, second_star = linked_lst.get_stars()
    return first_star * second_star

def main():
    assert(solve(TEST_INPUT, NUM_MOVES) == 149245887792)
    print(solve(INPUT, NUM_MOVES))

main()