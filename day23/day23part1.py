NUM_MOVES = 100

# TEST
# INPUT_TXT = '389125467'

INPUT_TXT = '315679824'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, input_string):
        self.access_dict = {}

        start = int(input_string[0])

        prev = None
        maxi = 0
        for elem in input_string:
            node = Node(int(elem))
            self.access_dict[int(elem)] = node
            if prev:
                self.access_dict[prev].next = node
            prev = int(elem)

            maxi = max(maxi, int(elem))

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


linked_lst = LinkedList(INPUT_TXT)
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

print(linked_lst.get_order())
