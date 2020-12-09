file = open('day9input.txt')

numbers = []
# preamble = 25
for line in file:
    line = line.strip('\n')
    numbers.append(int(line))

file.close()

start_pointer = 0
end_pointer = 0
total = 0

acc_total = 1721308972

while end_pointer < len(numbers):
    if total < acc_total:
        total += numbers[end_pointer]
        end_pointer += 1
    elif total > acc_total:
        total -= numbers[start_pointer]
        start_pointer += 1
    else:
        break

sub_lst = numbers[start_pointer: end_pointer]
print(min(sub_lst) + max(sub_lst))