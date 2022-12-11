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
while len(queue) > 0:
    x += queue.pop(0)
    pos +=1
    pixel = '#' if pos in range(x-1, x+2) else '.'
    screen[row].append(pixel)
    if(pos == 40):
        pos = 0;
        row +=1

for x in screen:
    p = ''
    for y in x:
        p += y
    print(p)
