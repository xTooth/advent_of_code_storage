file = open('input.txt', 'r')
lines = file.readlines()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
costs = {}
map = []
visited = set()
for line in lines:
    map.append([x for x in line.strip()])

for y, row in enumerate(map):
    for x, char in enumerate(row):
        if (y, x) not in visited:
            queue = []
            queue.append((y, x))
            size = 0
            fence = 0
            while queue:
                pos = queue.pop(0)
                if pos not in visited:
                    visited.add((pos[0], pos[1]))
                    size += 1
                    for direction in directions:
                        pos_y = direction[0] + pos[0]
                        pos_x = direction[1] + pos[1]
                        if 0 <= pos_y < len(map) and 0 <= pos_x < len(row):
                            if map[pos_y][pos_x] != char:
                                fence += 1
                            elif (pos_y, pos_x) not in visited and map[pos_y][pos_x] == char:  # noqa E501
                                queue.append((pos_y, pos_x))
                        else:
                            fence += 1
            costs[(y, x)] = (size, fence)
print(sum([a[0]*a[1] for a in costs.values()]))
