file = open('input.txt', 'r')
lines = file.readlines()

# read input
space = []
number = 0
for x in range(len(lines[0])):
    if x % 2 == 0:
        if int(lines[0][x]) > 0:
            space += [number for i in range(int(lines[0][x]))]
        number += 1
    else:
        if int(lines[0][x]) > 0:
            space += ['.' for i in range(int(lines[0][x]))]

# attempt to fill empty space
y = len(space) - 1
while y >= 0:
    if space[y] == '.':
        y -= 1
    else:
        # a given number can only exist in one group
        # -> count returns the size of the group
        amount_of_space_required = space.count(space[y])
        adjusted = False
        start_index = 0
        size = 0

        for i in range(y):
            if space[i] == '.':
                size += 1
                if size == 1:
                    start_index = i
                if size == amount_of_space_required:
                    break
            else:
                size = 0

        if size != 0:
            for i in range(amount_of_space_required):
                space[start_index] = space[y]
                space[y] = '.'
                y -= 1
                start_index += 1
        else:
            # skip rest of particular value
            y -= amount_of_space_required

# count sum
sum = 0

for x in range(len(space)):
    if space[x] != '.':
        sum += x * space[x]

print(sum)
