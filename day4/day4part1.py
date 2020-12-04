file = open('day4input.txt', 'r')

valid = 0 
data = []
for line in file:
    line = line.strip('\n')
    if not line:
        if len(data) == 8 or (len(data) == 7 and 'cid' not in data):
            valid += 1
        print(data)
        data = []
    else:
        info_parts = line.split(' ')
        # print(info_parts)
        for info in info_parts:
            data.append(info.split(':')[0])
        # print(data)

if data:
    if len(data) == 8 or (len(data) == 7 and 'cid' not in data):
        valid += 1
print(valid)
file.close()