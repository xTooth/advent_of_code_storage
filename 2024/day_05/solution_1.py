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
    index_map = {update[i]: i for i in range(len(update))}
    matches_rules = True
    for rule in required_orders:
        if rule[0] in index_map and rule[1] in index_map:
            if not index_map[rule[0]] < index_map[rule[1]]:
                matches_rules = False
                break
    if matches_rules:
        sum += update[int(len(update)/2)]
print(sum)
