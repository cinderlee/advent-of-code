file = open('day6input.txt')

sum_total = 0
answers = set()

for line in file:
    line = line.strip('\n')
    
    if not line:
        sum_total += len(answers)
        print(answers, len(answers))
        answers = set()

    else:
        for elem in line:
            answers.add(elem)

if len(answers) != 0:
    sum_total += len(answers)

print(sum_total)