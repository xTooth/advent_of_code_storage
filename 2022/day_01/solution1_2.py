file = open('input.txt', 'r')
lines = file.readlines()

def get_totals_list(lines):
    calories = []
    temp_calories = 0
    for line in lines:
        if len(line.strip()) == 0:  
            calories.append(temp_calories)
            temp_calories = 0
        else:
            temp_calories += int(line)
    return calories
  
list = sorted(get_totals_list(lines),reverse=True)
sum = 0
for i in range(0, 3):
    sum += list[i]
print(sum)