'''
    a = 1, rock
    b = 2, paper
    c = 3, scissors
    
    x = lose
    y = draw
    z = win

    win  +6
    draw +3
    loss +0
'''

points_dict = {
    'X': 0,
    'Y': 1,
    'Z': 2,
    'A': 0,
    'B': 1,
    'C': 2
}

points_array = [
   # R P S
    [4,1,7],    # rock 
    [8,5,2],    # paper 
    [3,9,6]     # scissors 
]

file = open('input.txt', 'r')
lines = file.readlines()

total_points = 0;
for line in lines:
    line_as_list = line.strip().split(' ')
    opponents_choise = line_as_list[0]
    own_choise = line_as_list[1]
    total_points += points_array[points_dict[own_choise]][points_dict[opponents_choise]]

print(total_points)