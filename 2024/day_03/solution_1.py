import re


file = open('input.txt', 'r')
lines = file.readlines()

x = ""
for line in lines:
    x += line

y = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', x)
sum = 0
for finds in y:
    found = re.findall(r'[0-9]{1,3}', finds)
    sum += int(found[0]) * int(found[1])

print(sum)
