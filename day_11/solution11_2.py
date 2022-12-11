monkeys = [
    {
        'items': [97, 81, 57, 57, 91, 61],
        'operation': lambda x: x * 7,
        'test': lambda x: x % 11 == 0,
        'pass': 5,
        'fail': 6
    },
    {
        'items': [88, 62, 68, 90],
        'operation': lambda x: x * 17,
        'test': lambda x: x % 19 == 0,
        'pass': 4,
        'fail': 2
    },
    {
        'items': [74, 87],
        'operation': lambda x: x + 2,
        'test': lambda x: x % 5 == 0,
        'pass': 7,
        'fail': 4
    },
    {
        'items': [53, 81, 60, 87, 90, 99, 75],
        'operation': lambda x: x + 1,
        'test': lambda x: x % 2 == 0,
        'pass': 2,
        'fail': 1
    },
    {
        'items': [57],
        'operation': lambda x: x + 6,
        'test': lambda x: x % 13 == 0,
        'pass': 7,
        'fail': 0
    },
    {
        'items': [54, 84, 91, 55, 59, 72, 75, 70],
        'operation': lambda x: x * x,
        'test': lambda x: x % 7 == 0,
        'pass': 6,
        'fail': 3
    },
    {
        'items': [95, 79, 79, 68, 78],
        'operation': lambda x: x + 3,
        'test': lambda x: x % 3 == 0,
        'pass': 1,
        'fail': 3
    },
    {
        'items': [61, 97, 67],
        'operation': lambda x: x + 4,
        'test': lambda x: x % 17 == 0,
        'pass': 0,
        'fail': 5
    }
]

lcm = 17*3*7*13*2*5*19*11 # cant claim credit for this idea - thx reddit: https://www.reddit.com/r/adventofcode/comments/zifqmh/2022_day_11_solutions/
 
operations = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0,10000):
    for j in range(0,len(monkeys)):
        operations[j] += len(monkeys[j]['items'])
        while len(monkeys[j]['items']) > 0:
            testable = monkeys[j]['operation'](monkeys[j]['items'].pop(0))
            if monkeys[j]['test'](testable):
                monkeys[monkeys[j]['pass']]['items'].append(testable%lcm)
            else:
                monkeys[monkeys[j]['fail']]['items'].append(testable%lcm)
operations.sort(reverse=True)
print(operations[0]*operations[1])