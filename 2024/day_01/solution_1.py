file = open('input.txt', 'r')
lines = file.readlines()

# read input
left_list = []
right_list = []
for line in lines:
    left_list.append(int(line.split('   ')[0]))
    right_list.append(int(line.split('   ')[1]))


# calc_total_distance
total = 0
left_list.sort()
right_list.sort()
for x in range(0, len(left_list)):
    total += abs(left_list[x] - right_list[x])

print(total)

# this is both stupid and pointless - but fun. the hole in one solution
print(sum([abs(value - sorted([int(line.split()[1]) for line in open('input.txt', 'r').readlines()])[index]) for index, value in enumerate(sorted([int(line.split()[0]) for line in open('input.txt', 'r').readlines()]))]))  # noqa E501
