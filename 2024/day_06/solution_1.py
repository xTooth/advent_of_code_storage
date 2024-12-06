def get_dir(y, x):   # return (y,x)
    if x == 1 and y == 0:
        return (1, 0)
    if x == -1 and y == 0:
        return (-1, 0)
    if x == 0 and y == 1:
        return (0, -1)
    return (0, 1)


# read file into map
file = open('input.txt', 'r')
lines = file.readlines()

map = []
for line in lines:
    map.append([x for x in line if x != '\n'])

# set starting position
guard_pos = (0, 0)
guard_dir = (0, 0)
route_len: set[tuple[int, int]] = set()

for y in range(len(map)):
    for x in range(len(map[0])):
        if '^' in map[y][x]:
            guard_pos = (y, x)
            guard_dir = (-1, 0)
            route_len.add((y, x))
            break
        if 'v' in map[y][x]:
            guard_pos = (y, x)
            guard_dir = (1, 0)
            route_len.add((y, x))
            break
        if '<' in map[y][x]:
            guard_pos = (y, x)
            guard_dir = (0, -1)
            route_len.add((y, x))
            break
        if '>' in map[y][x]:
            guard_pos = (y, x)
            guard_dir = (0, 1)
            route_len.add((y, x))
            break
# move guard
while (guard_pos[0] < len(map) and guard_pos[1] < len(map[0])):
    new_pos_x = guard_pos[1] + guard_dir[1]
    new_pos_y = guard_pos[0] + guard_dir[0]
    if (
        new_pos_x >= len(map[0]) or
        new_pos_y >= len(map) or
        new_pos_x < 0 or
        new_pos_y < 0
    ):
        break
    if map[new_pos_y][new_pos_x] == '#':
        guard_dir = get_dir(guard_dir[0], guard_dir[1])
    else:
        guard_pos = (new_pos_y, new_pos_x)
        route_len.add(guard_pos)

print(len(route_len))
