MAX_NUM = 1000000
NUM_MOVES = 10000000

# TEST
# INPUT_TXT = '389125467'

INPUT_TXT = '315679824'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, input_lst):
        self.access_dict = {}

        start = input_lst[0]

        prev = None
        maxi = 0
        for elem in input_lst:
            node = Node(elem)
            self.access_dict[elem] = node
            if prev:
                self.access_dict[prev].next = node
            prev = elem

            maxi = max(maxi, elem)

        self.access_dict[prev].next = self.access_dict[start]
        self.maxi = maxi

    def get_cup(self,num):
        return self.access_dict[num]

    def get_max(self):
        return self.maxi

    def get_order(self):
        lst = []
        curr_cup = self.get_cup(1).next

        while curr_cup.data != 1:
            lst.append(str(curr_cup.data))
            curr_cup = curr_cup.next

        return ''.join(lst)

    def get_stars(self):
        first_star = self.get_cup(1).next
        second_star = first_star.next

        return first_star.data, second_star.data

def generate_input_list():
    input_lst = [int(elem) for elem in INPUT_TXT]
    maxi = max(input_lst)
    for elem in range(maxi + 1, MAX_NUM + 1):
        input_lst.append(elem)

    return input_lst

input_list = generate_input_list()
linked_lst = LinkedList(input_list)
maxi = linked_lst.get_max()
curr_cup = linked_lst.get_cup(int(INPUT_TXT[0]))
count = 0

while count < NUM_MOVES:
    first_cup = curr_cup.next
    second_cup = first_cup.next
    third_cup = second_cup.next

    curr_cup.next = third_cup.next

    three_cups_data = [first_cup.data, second_cup.data, third_cup.data]

    next_cup = curr_cup.data 

    while True:
        next_cup -= 1
        if next_cup == 0:
            next_cup = maxi
        if next_cup in three_cups_data:
            continue
        else:
            next_node = linked_lst.get_cup(next_cup)
            after = next_node.next
            next_node.next = first_cup
            third_cup.next = after
            break

    count += 1
    curr_cup = curr_cup.next

first_star, second_star = linked_lst.get_stars()
print(first_star * second_star)
