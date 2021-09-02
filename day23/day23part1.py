NUM_MOVES = 100

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
    A crab wants to play a game with cups ordered clockwise in the input text.
    The first number in the input is the current cup and the crab is going to 
    perform a number of moves,

    Returns the order of cups after the cup labeled 1.
    '''
    linked_lst = LinkedList(input_txt)
    start_cup = int(input_txt[0])
    play_crab_game(linked_lst, start_cup, num_moves)

    return linked_lst.get_post_order(1)

def main():
    assert(solve(TEST_INPUT, NUM_MOVES) == '67384529')
    print(solve(INPUT, NUM_MOVES))

main()