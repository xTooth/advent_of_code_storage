file = open('input.txt', 'r')
lines = file.readlines()

map = []
hilltops = []
for y, line in enumerate(lines):
    map.append([])
    for x, char in enumerate(line.strip()):
        map[y].append(int(char))
        if int(char) == 9:
            hilltops.append((y, x))

print(map)
ans = 0

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for hilltop in hilltops:
    queue = [hilltop]
    while queue:
        pos = queue.pop(0)
        if map[pos[0]][pos[1]] == 0:
            ans += 1
        else:
            for move in moves:
                new_y = pos[0] + move[0]
                new_x = pos[1] + move[1]
                if 0 <= new_y < len(map) and 0 <= new_x < len(map[0]):
                    if map[pos[0] + move[0]][pos[1] + move[1]] == map[pos[0]][pos[1]] - 1:  # noqa E501
                        queue.append((pos[0] + move[0], pos[1] + move[1]))

print(ans)
