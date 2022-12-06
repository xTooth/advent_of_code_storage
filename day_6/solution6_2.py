file = open('input.txt', 'r')
line = file.readlines()[0]

required_len = 14
for i in range(required_len,len(line)):
    if(len(set(line[(i-required_len):i])) == required_len):
        print(i)
        break;