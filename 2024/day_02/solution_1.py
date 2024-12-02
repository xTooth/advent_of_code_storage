file = open('input.txt', 'r')
lines = file.readlines()
total_ok_reports = 0

for line in lines:
    content = [int(x) for x in line.split()]

    if all(
        content[i] - content[i+1] >= 1
        and content[i] - content[i+1] <= 3
        for i in range(len(content) - 1)
    ):
        total_ok_reports += 1
    if all(
        content[i + 1] - content[i] >= 1
        and content[i + 1] - content[i] <= 3
        for i in range(len(content) - 1)
    ):
        total_ok_reports += 1
print(total_ok_reports)
