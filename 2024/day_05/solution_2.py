file = open('input.txt', 'r')
lines = file.readlines()

required_orders = []
updates = []
for line in lines:
    if '|' in line:
        x = line.split('|')
        required_orders.append((int(x[0]), int(x[1])))
    if ',' in line:
        updates.append([int(x) for x in line.split(',')])

sum = 0
for update in updates:
    count_this = False
    count = 0
    while count < len(required_orders):
        if count < len(required_orders):
            count = 0
        for rule in required_orders:
            index_map = {update[i]: i for i in range(len(update))}
            if rule[0] in index_map and rule[1] in index_map:
                if not index_map[rule[0]] < index_map[rule[1]]:
                    count_this = True
                    old_index = index_map[rule[0]]
                    index_map[rule[0]] = index_map[rule[1]]
                    index_map[rule[1]] = old_index
                    reverse_index_map = {y: x for x, y in index_map.items()}
                    update = [
                        reverse_index_map[i] for i in range(0, len(update))
                        ]
                else:
                    count += 1
            else:
                count += 1
    if count_this:
        sum += update[int(len(update)/2)]
print(sum)
