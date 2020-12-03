file = open('day3input.txt', 'r')

arr = []
for line in file:
    lst = []
    for elem in line.strip('\n'):
        lst.append(elem)
    arr.append(lst)

file.close()

trees = 0
x = 0 
y = 0 

while x < len(arr):
    if arr[x][y] == '#':
        trees += 1
    x += 1
    y = (y + 3) % len(arr[0])


print(trees)