file = open('input.txt', 'r')
lines = file.readlines()


# read input
left_list = []
right_list = []
for line in lines:
    left_list.append(int(line.split('   ')[0]))
    right_list.append(int(line.split('   ')[1]))

# collect appearances
appearances = {}
for x in right_list:
    if x in appearances:
        appearances[x] += 1
    else:
        appearances[x] = 1

# calc totals
totals = 0
for number in left_list:
    totals += number * appearances.get(number, 0)

print(totals)
