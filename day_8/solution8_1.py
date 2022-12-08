file = open('input.txt', 'r')
lines = file.readlines()

def _return_list_of_zeros(len: int):
    return [0] * len


def check_visible(y, x, largest_num):
    if(int(input[y][x]) > largest_num):
        largest_num = int(input[y][x])
        visible[y][x] = 1
    return largest_num


input = []
visible = []
for line in lines:
    trees = line.strip()
    input.append(list(trees))
    visible.append(_return_list_of_zeros(len(input[-1])))

# check x -> 
for y in range(0, len(input)):
    largest_num = -6
    for x in range(0,len(input[0])):
        largest_num = check_visible(y=y, x=x, largest_num=largest_num)

# check x <-
for y in range(0, len(input)):
    largest_num = -6
    for x in range(len(input[0])-1, -1, -1):
        largest_num = check_visible(y=y, x=x, largest_num=largest_num)

# check y -> 
for x in range(0, len(input)):
    largest_num = -6
    for y in range(0,len(input[0])):
        largest_num = check_visible(y=y, x=x, largest_num=largest_num)

# check y <-
for x in range(0, len(input)):
    largest_num = -6
    for y in range(len(input[0])-1, -1, -1):
        largest_num = check_visible(y=y, x=x, largest_num=largest_num)

summ = 0
print(visible)
for x in visible:
    summ += sum(x)

print(summ)