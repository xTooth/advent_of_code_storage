file = open('input.txt', 'r')
lines = file.readlines()
queue = []
x = 1
pos = 1
for line in lines:
    movement = line.strip().split(' ')
    queue.append(0)
    if len(movement ) > 1:
        queue.append(int(movement[1]))
sum = 0
while len(queue) > 0:
    pos +=1
    x += queue.pop(0)
    if (pos - 20) % 40 == 0:
        sum += pos * x

print(sum)