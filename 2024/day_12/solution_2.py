

file = open('input.txt', 'r')
lines = file.readlines()


def count_corners(pos, char, map):
    corners = 0
    pos_y = pos[0]
    pos_x = pos[1]
    # outside corners
    if map.get((pos_y, pos_x + 1), '_') != char and map.get((pos_y + 1, pos_x), '_') != char:
        corners += 1
    if map.get((pos_y, pos_x + 1), '_') != char and map.get((pos_y - 1, pos_x), '_') != char:
        corners += 1
    if map.get((pos_y, pos_x - 1), '_') != char and map.get((pos_y + 1, pos_x), '_') != char:
        corners += 1
    if map.get((pos_y, pos_x - 1), '_') != char and map.get((pos_y - 1, pos_x), '_') != char:
        corners += 1
    # inside corners
    if map.get((pos_y, pos_x + 1), '_') == char and map.get((pos_y + 1, pos_x), '_') == char and map.get((pos_y + 1, pos_x + 1), '_') != char:
        corners += 1
    if map.get((pos_y, pos_x + 1), '_') == char and map.get((pos_y - 1, pos_x), '_') == char and map.get((pos_y - 1, pos_x + 1), '_') != char:
        corners += 1
    if map.get((pos_y, pos_x - 1), '_') == char and map.get((pos_y + 1, pos_x), '_') == char and map.get((pos_y + 1, pos_x - 1), '_') != char:
        corners += 1
    if map.get((pos_y, pos_x - 1), '_') == char and map.get((pos_y - 1, pos_x), '_') == char and map.get((pos_y - 1, pos_x - 1), '_') != char:
        corners += 1
    return corners


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
costs = {}
map = []
map_dict: dict[tuple[int, int], str] = {}
visited = set()
for y, line in enumerate(lines):
    map.append([x for x in line.strip()])
    for x, char in enumerate(line.strip()):
        map_dict[(y, x)] = char

for y, row in enumerate(map):
    for x, char in enumerate(row):
        if (y, x) not in visited:
            queue = []
            queue.append((y, x))
            size = 0
            corners = 0
            while queue:
                pos = queue.pop(0)
                if pos not in visited:
                    visited.add((pos[0], pos[1]))
                    size += 1
                    corners += count_corners(pos, char, map_dict)
                    for direction in directions:
                        pos_y = direction[0] + pos[0]
                        pos_x = direction[1] + pos[1]
                        if 0 <= pos_y < len(map) and 0 <= pos_x < len(row):
                            if (pos_y, pos_x) not in visited and map[pos_y][pos_x] == char:
                                queue.append((pos_y, pos_x))

            costs[(y, x)] = (size, corners)
print(sum([a[0]*a[1] for a in costs.values()]))
