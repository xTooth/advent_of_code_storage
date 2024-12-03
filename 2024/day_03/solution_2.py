import re


def get_sum(x):
    sum = 0
    y = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', x)
    for finds in y:
        found = re.findall(r'[0-9]{1,3}', finds)
        sum += int(found[0]) * int(found[1])
    return sum


file = open('input.txt', 'r')
lines = file.readlines()

x = ""
for line in lines:
    x += line

split = x.split("don't()")
ans = 0
for i in range(0, len(split)):
    if i == 0:
        ans += get_sum(split[i])
    else:
        a = 1
        split_split = split[i].split('do()')
        for a in range(1, len(split_split)):
            ans += get_sum(split_split[a])

print(ans)
