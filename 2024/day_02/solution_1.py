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


# this is truly awful
print(sum([1 for line in open('input.txt', 'r').readlines() if all(int(line.split()[i]) - int(line.split()[i + 1]) >= 1 and int(line.split()[i]) - int(line.split()[i + 1]) <= 3 for i in range(len(line.split())-1)) or all(int(line.split()[i + 1]) - int(line.split()[i]) >= 1 and int(line.split()[i + 1]) - int(line.split()[i]) <= 3 for i in range(len(line.split())-1))]))  # noqa E501
