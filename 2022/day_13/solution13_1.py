def compare(line_one, line_two):
    pass


def build(line):
    creation = []
    split_line = line[1:-1].split(',')
    print(split_line)
    return creation

file = open('input.txt', 'r')
lines = file.readlines()

line_one = []
line_two = []
for line in lines:
    line = line.strip()
    if len(line) == 0:
        compare(line_one, line_two)
        line_one = []
        line_two = []
    if len(line_one) == 0:
        line_one = build(line)
    else:
        line_two = build(line)