file = open('input.txt', 'r')
lines = file.readlines()

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


x = 0
y = len(space) - 1
while x < y and y > 0:
    if space[x] == '.' and space[y] != '.':
        space[x] = space[y]
        space[y] = '.'
        x += 1
        y -= 1
    if space[x] != '.':
        x += 1
    if space[y] == '.':
        y -= 1

sum = 0
for x in range(len(space)):
    if space[x] != '.':
        sum += x * space[x]

print(sum)
