file = open('input.txt', 'r')
lines = file.readlines()
queue = []
x = 1
pos = 0
for line in lines:
    movement = line.strip().split(' ')
    queue.append(0)
    if len(movement ) > 1:
        queue.append(int(movement[1]))

screen = [[],[],[],[],[],[]]
row = 0
pos = 0
while len(queue) > 0:
    pos += 1
    x += queue.pop(0)
    pixel = '#' if pos in {x-1, x, x+1} else '.'
    screen[row].append(pixel)
    if len(screen[row]) == 40:
        row +=1
        pos = 0

for x in screen:
    p = '..#'
    for y in x:
        p += y
    print(p)
