file = open('day3input.txt', 'r')

arr = []
for line in file:
    lst = []
    for elem in line.strip('\n'):
        lst.append(elem)
    arr.append(lst)

file.close()

def tree_slope(slope_x, slope_y):
    trees = 0
    x = 0 
    y = 0 

    while x < len(arr):
        if arr[x][y] == '#':
            trees += 1
        x += slope_x
        y = (y + slope_y) % len(arr[0])

    return trees

print(tree_slope(1,3))

a = tree_slope(1, 1)
b = tree_slope(1, 3)
c = tree_slope(1, 5)
d = tree_slope(1, 7)
e = tree_slope(2, 1)

print(a * b * c * d * e)