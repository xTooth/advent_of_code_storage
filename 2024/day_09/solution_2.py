file = open('input.txt', 'r')
lines = file.readlines()

# read input
number_of_elements_map = {}
space = []
number = 0
for x in range(len(lines[0])):
    if x % 2 == 0:
        if int(lines[0][x]) > 0:
            space += [number for i in range(int(lines[0][x]))]
            number_of_elements_map[number] = int(lines[0][x])
        number += 1
    else:
        if int(lines[0][x]) > 0:
            space += ['.' for i in range(int(lines[0][x]))]

# find index and size of empty space
x = 0
empty_space_index_to_size = {}
while x < len(space):
    if space[x] == '.':
        index = x
        size = 0
        while space[x] == '.':
            size += 1
            x += 1
        empty_space_index_to_size[index] = size
    x += 1

# attempt to fill empty space
y = len(space) - 1
while y >= 0:
    if space[y] == '.':
        y -= 1
    else:
        amount_of_space_required = number_of_elements_map[space[y]]
        adjusted = False
        for key, val in empty_space_index_to_size.items():
            if val >= amount_of_space_required and key < y:
                adjusted = True
                index = key
                size = val
                del empty_space_index_to_size[index]
                empty_space_index_to_size[index + amount_of_space_required] = val - amount_of_space_required
                char = space[y]
                while space[y] == char:
                    space[index] = space[y]
                    space[y] = '.'
                    y -= 1
                    index += 1
                break
        if not adjusted:
            # skip rest of particular value
            y -= amount_of_space_required


# count sum
sum = 0

for x in range(len(space)):
    if space[x] != '.':
        sum += x * space[x]

print(sum)
