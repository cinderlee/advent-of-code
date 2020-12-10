# file = open('day10testinput2.txt')
file = open('day10input.txt')

lst = [0]
for line in file:
    line = line.strip('\n')
    lst.append(int(line))

file.close()

num_paths = {} 

# we only care about if the numbers are within 3 
num_paths[0] = 1

def populate_path(index, lst, num_paths):
    num = 0
    ptr = index - 1
    while ptr >= 0 and lst[index] - lst[ptr] <= 3:
        num += num_paths[lst[ptr]]
        ptr -= 1
    num_paths[lst[index]] = num

lst.sort()
for index in range(1, len(lst)):
    populate_path(index, lst, num_paths)

print(num_paths[max(lst)])


