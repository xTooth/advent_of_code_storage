file = open('input.txt', 'r')
lines = file.readlines()

total_intersections = 0

for line in lines:
    values = line.strip().split(',')
    range1 = set(range(int(values[0].split('-')[0]),int(values[0].split('-')[1])+1))
    range2 = set(range(int(values[1].split('-')[0]),int(values[1].split('-')[1])+1))
    if (range1.issubset(range2) or range2.issubset(range1)):
        total_intersections +=1
print(total_intersections)