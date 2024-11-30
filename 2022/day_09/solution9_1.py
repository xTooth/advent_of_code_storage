head_x = 0
head_y = 0
tail_x = 0
tail_y = 0
tail_locations = {(0,0)}


def move_vertically():
    global head_y
    global tail_x
    global tail_y
    if tail_y < head_y:
        tail_y += 1
    else:
        tail_y -= 1
    tail_locations.add((tail_x,tail_y))

def move_sideways():
    global head_x
    global tail_x
    global tail_y
    if tail_x < head_x:
        tail_x += 1
    else:
        tail_x -= 1
    tail_locations.add((tail_x,tail_y))

def move_diagonally():
    global head_x
    global head_y
    global tail_x
    global tail_y
    if tail_x < head_x:
        tail_x += 1
    else:
        tail_x -= 1
    if tail_y < head_y:
        tail_y += 1
    else:
        tail_y -= 1
    tail_locations.add((tail_x,tail_y))

def move_tail_if_required(max_allowed_distance):
    global head_x
    global head_y
    global tail_x
    global tail_y
    if abs(head_x - tail_x) > max_allowed_distance:
        if abs(head_y - tail_y) > 0:
            move_diagonally()
        else:
            move_sideways()
    if abs(head_y - tail_y) > max_allowed_distance:
        if abs(head_x - tail_x) > 0:
            move_diagonally()
        else:
            move_vertically()

def move_right(length):
    global head_x
    for i in range(0,length):
        head_x += 1
        move_tail_if_required(1)


def move_left(length):
    global head_x
    for i in range(0,length):
        head_x -= 1
        move_tail_if_required(1)


def move_up(length):
    global head_y
    for i in range(0,length):
        head_y += 1
        move_tail_if_required(1)
   

def move_down(length):
    global head_y
    for i in range(0,length):
        head_y -= 1
        move_tail_if_required(1)
    




file = open('input.txt', 'r')
lines = file.readlines()
for line in lines:
    movement = line.strip().split(' ')
    direction = movement[0]
    length = int(movement[1])

    match direction:
        case 'R':
            move_right(length)
        case 'L':
            move_left(length)
        case 'U':
            move_up(length)
        case _:
            move_down(length)

print(len(tail_locations))
