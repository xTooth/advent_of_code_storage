def get_antinode_locations(location_a, location_b, map_height, map_width):
    if location_a[0] > location_b[0]:
        antinode_1_y = location_a[0] + abs(location_b[0] - location_a[0])
        antinode_2_y = location_b[0] - abs(location_b[0] - location_a[0])
    else:
        antinode_1_y = location_a[0] - abs(location_b[0] - location_a[0])
        antinode_2_y = location_b[0] + abs(location_b[0] - location_a[0])
    if location_a[1] > location_b[1]:
        antinode_1_x = location_a[1] + abs(location_b[1] - location_a[1])
        antinode_2_x = location_b[1] - abs(location_b[1] - location_a[1])
    else:
        antinode_1_x = location_a[1] - abs(location_b[1] - location_a[1])
        antinode_2_x = location_b[1] + abs(location_b[1] - location_a[1])
    r = set()
    if 0 <= antinode_1_x < map_width and 0 <= antinode_1_y < map_height:
        r.add((antinode_1_y, antinode_1_x))
    if 0 <= antinode_2_x < map_width and 0 <= antinode_2_y < map_height:
        r.add((antinode_2_y, antinode_2_x))
    return r


file = open('input.txt', 'r')
lines = file.readlines()

map: list[list[str]] = []
for line in lines:
    map.append([x for x in line if x != '\n'])

map_height = len(map)
map_width = len(map[0])
location_dict = {}

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] != '.':
            if map[y][x] not in location_dict:
                location_dict[map[y][x]] = []
            location_dict[map[y][x]].append((y, x))

ans = set()

for char, locations in location_dict.items():
    i = 0
    temp = set()
    for i in range(len(locations)-1):
        for ii in range(i+1, len(locations)):
            temp.update(
                get_antinode_locations(
                    locations[i],
                    locations[ii],
                    map_height,
                    map_width
                )
            )

    for item in temp:
        ans.update(temp)

print(len(ans))
