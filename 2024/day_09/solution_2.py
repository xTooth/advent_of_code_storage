file = open('input.txt', 'r')
lines = file.readlines()

# read input
space = []
number = 0
for index, value in enumerate(lines[0]):
    if int(value) > 0:
        if index % 2 == 0:
            space += [number for i in range(int(value))]
            number += 1
        else:
            space += ['.' for i in range(int(value))]

# attempt to fill empty space
data_index = len(space) - 1
while data_index >= 0:
    if space[data_index] == '.':
        data_index -= 1
    else:
        # a given number can only exist in one group
        # -> count returns the size of the group
        amount_of_space_required = space.count(space[data_index])
        start_index = 0
        size = 0

        for i in range(data_index):
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
                space[start_index] = space[data_index]
                space[data_index] = '.'
                data_index -= 1
                start_index += 1
        else:
            # skip rest of particular value
            data_index -= amount_of_space_required

print(sum([x * y for x, y in enumerate(space) if y != '.']))
