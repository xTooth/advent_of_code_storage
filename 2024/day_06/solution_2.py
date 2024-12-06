from copy import deepcopy


def get_dir(y, x):   # return (y,x)
    if x == 1 and y == 0:
        return (1, 0)
    if x == -1 and y == 0:
        return (-1, 0)
    if x == 0 and y == 1:
        return (0, -1)
    return (0, 1)


def is_within_map_bounds(y, x, map):
    return (
            x < len(map[0]) and
            y < len(map) and
            x >= 0 and
            y >= 0
        )


def can_cause_loop(
        gp: tuple[int, int],
        d: tuple[int, int],
        m: list[list[int]],
        r: set[tuple[int, int, int, int]]
) -> bool:
    while (gp[0] < len(m) and gp[1] < len(m[0])):
        npx = gp[1] + d[1]
        npy = gp[0] + d[0]
        if not is_within_map_bounds(npy, npx, map):
            break
        if m[npy][npx] == '#':
            d = get_dir(d[0], d[1])
        else:
            if (npy, npx, d[0], d[1]) in r:
                return True
            else:
                gp = (npy, npx)
                r.add((npy, npx, d[0], d[1]))
    return False


# read file into map
file = open('input.txt', 'r')
lines = file.readlines()

map = []
for line in lines:
    map.append([x for x in line if x != '\n'])

# set starting position
guard_pos = (0, 0)
guard_dir = (0, 0)
obstacles: set[tuple[int, int]] = set()
route: set[tuple[int, int, int, int]] = set()  # (y, x, dir_y, dir_x)
visited: set[tuple[int, int]] = set()
for y in range(len(map)):
    for x in range(len(map[0])):
        if '^' in map[y][x]:
            guard_pos = (y, x)
            guard_dir = (-1, 0)
            route.add((y, x, -1, 0))
            break
        if 'v' in map[y][x]:
            guard_pos = (y, x)
            guard_dir = (1, 0)
            route.add((y, x, 1, 0))
            break
        if '<' in map[y][x]:
            guard_pos = (y, x)
            guard_dir = (0, -1)
            route.add((y, x, 0, -1))
            break
        if '>' in map[y][x]:
            guard_pos = (y, x)
            guard_dir = (0, 1)
            route.add((y, x, 0, 1))
            break


# move guard
while is_within_map_bounds(guard_pos[0], guard_pos[1], map):
    visited.add(guard_pos)
    new_pos_x = guard_pos[1] + guard_dir[1]
    new_pos_y = guard_pos[0] + guard_dir[0]
    if not is_within_map_bounds(new_pos_y, new_pos_x, map):
        break
    if map[new_pos_y][new_pos_x] == '#':
        guard_dir = get_dir(guard_dir[0], guard_dir[1])
    else:
        guard_pos = (new_pos_y, new_pos_x)
        temp_map = deepcopy(map)
        route.add((guard_pos[0], guard_pos[1], guard_dir[0], guard_dir[1]))
        temp_obstacle_y = new_pos_y + guard_dir[0]
        temp_obstacle_x = new_pos_x + guard_dir[1]
        if is_within_map_bounds(
            temp_obstacle_y,
            temp_obstacle_x,
            map
        ):
            temp_map[temp_obstacle_y][temp_obstacle_x] = '#'

        if (
            (temp_obstacle_y, temp_obstacle_x) not in visited
            and can_cause_loop(
                    deepcopy(guard_pos),
                    guard_dir,
                    temp_map,
                    deepcopy(route)
                )
        ):
            obstacles.add((
                temp_obstacle_y,
                temp_obstacle_x
            ))
print(obstacles)
print(len(obstacles))  # 1284 - wrong answer.

'''
Test input obstacles:
    6,3
    7,6
    7,7
    8,1
    8,3
    9,7
'''
