'''
{
    'dir_name': {    
        'own_size': 'dir_size',
        'sub_dirs': [dir_names...]
    }
}
'''

current_location = []
current_location_name = ''
info_dict = {}

file = open('input.txt', 'r')
lines = file.readlines()

for line in lines:
    commands = line.strip().split(' ')
    if commands[1] == 'cd' and commands[2] != '..':
        current_location.append(f'_{commands[2]}')
        current_location_name = ''.join(current_location)
        if not info_dict.get(current_location_name):
            info_dict[current_location_name] = {
                'own_size': 0,
                'sub_dirs': []
            }
    elif commands[0] == 'dir':
        sub_dir_name = current_location_name + '_' + commands[1]
        info_dict[current_location_name]['sub_dirs'].append(sub_dir_name)
    elif commands[0].isnumeric():
        info_dict[current_location_name]['own_size'] += int(commands[0])
    else:
        if commands[1] == 'cd' and commands[2] == '..':
            current_location.pop()
            current_location_name = ''.join(current_location)


def calculate_value(d: dict):
    val = d['own_size']
    if(len(d['sub_dirs']) > 0):
        for x in d['sub_dirs']:
            val += calculate_value(info_dict[x])
    return val


sum = calculate_value(info_dict['_/'])
current  = sum

for k, d in info_dict.items():
    temp_sum = calculate_value(d)
    if sum - temp_sum <= 40_000_000 and temp_sum < current:
        current = temp_sum
print(current)
