from copy import deepcopy


def is_safe(content):
    if all(
        content[i] - content[i+1] >= 1
        and content[i] - content[i+1] <= 3
        for i in range(len(content) - 1)
    ):
        return True
    if all(
        content[i + 1] - content[i] >= 1
        and content[i + 1] - content[i] <= 3
        for i in range(len(content) - 1)
    ):
        return True
    return False


def find_safe_brute_force(x):
    if is_safe(x):
        return 1
    else:
        for i in range(0, len(x)):
            cc = deepcopy(x)
            cc.pop(i)
            if is_safe(cc):
                return 1
    return 0


file = open('input.txt', 'r')
lines = file.readlines()
total_ok_reports = 0
for line in lines:
    content = [int(x) for x in line.split()]
    total_ok_reports += find_safe_brute_force(content)
print(total_ok_reports)
