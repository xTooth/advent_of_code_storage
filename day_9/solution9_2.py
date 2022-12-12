tail_locations = {(0,0)}
worm = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

def move_vertically(current_slot):
    if worm[current_slot][1] < worm[current_slot-1][1]:
        worm[current_slot] = (worm[current_slot][0], worm[current_slot][1] + 1)
    else:
        worm[current_slot] = (worm[current_slot][0], worm[current_slot][1] - 1)

def move_sideways(current_slot):
    if worm[current_slot][0] < worm[current_slot-1][0]:
        worm[current_slot] = (worm[current_slot][0] + 1, worm[current_slot][1])
    else:
        worm[current_slot] = (worm[current_slot][0] - 1, worm[current_slot][1])

def move_diagonally(current_slot):
    move_vertically(current_slot)
    move_sideways(current_slot)


def move_tail_if_required(current_slot, max_allowed_distance):
    if abs(worm[current_slot-1][0] - worm[current_slot][0]) > max_allowed_distance:
        if abs(worm[current_slot-1][1] - worm[current_slot][1]) > 0:
            move_diagonally(current_slot)
        else:
            move_sideways(current_slot)
    if abs(worm[current_slot-1][1] - worm[current_slot][1]) > max_allowed_distance:
        if abs(worm[current_slot-1][0] - worm[current_slot][0]) > 0:
            move_diagonally(current_slot)
        else:
            move_vertically(current_slot)

def move_right(length):
    for i in range(0,length):
        worm[0] = (worm[0][0] + 1, worm[0][1])
        for j in range(1, len(worm)):
            move_tail_if_required(j, 1)
        tail_locations.add(worm[9])


def move_left(length):
    for i in range(0,length):
        worm[0] = (worm[0][0] - 1, worm[0][1])
        for j in range(1, len(worm)):
            move_tail_if_required(j, 1)
        tail_locations.add(worm[9])

def move_up(length):
    for i in range(0,length):
        worm[0] = (worm[0][0], worm[0][1] + 1)
        for j in range(1, len(worm)):
            move_tail_if_required(j, 1)
        tail_locations.add(worm[9])
   

def move_down(length):
    for i in range(0,length):
        worm[0] = (worm[0][0], worm[0][1] - 1)
        for j in range(1, len(worm)):
            move_tail_if_required(j, 1)
        tail_locations.add(worm[9])    




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
