def recursion(index, test_score, numbers, total, operator):
    if index == len(numbers):
        return total == test_score

    if operator == '+':
        new_total = total + numbers[index]
    elif operator == '*':
        new_total = total * numbers[index]
    else:
        new_total = int(str(total) + str(numbers[index]))
    return (
        recursion(index + 1, test_score, numbers,  new_total, '+')
        or recursion(index + 1, test_score, numbers,  new_total, '*')
        or recursion(index + 1, test_score, numbers,  new_total, '||')
    )


file = open('input.txt', 'r')
lines = file.readlines()

ans = 0

for line in lines:
    values = line.split()
    ts = int(values[0].split(':')[0])
    numbers = [int(x) for x in values[1:]]
    if (
        recursion(1, ts, numbers, numbers[0], '+')
        or recursion(1, ts, numbers, numbers[0], '*')
        or recursion(1, ts, numbers, numbers[0], '||')
    ):
        ans += ts
print(ans)
