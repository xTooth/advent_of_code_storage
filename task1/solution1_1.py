file = open('input.txt', 'r')
lines = file.readlines()

max_calories = 0
temp_calories = 0

for line in lines:
    if len(line) <= 2:
        if(max_calories < temp_calories):
            max_calories = temp_calories
        temp_calories = 0
    else:
        temp_calories += int(line)

print(max_calories)