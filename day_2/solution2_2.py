'''
    x, a = 1, rock
    y, b = 2, paper
    z, c = 3, scissors

    win +6
    draw +3
    loss +0
'''

choises_dict = {
    'X': 0, # Lose
    'Y': 1, # Draw
    'Z': 2, # Win
    'A': 0, # Rock
    'B': 1, # Paper
    'C': 2  # Scissors
}

points_array = [
  #  r p s
    [3,1,2],    # Lose
    [4,5,6],    # draw
    [8,9,7]     # win
]

file = open('input.txt', 'r')
lines = file.readlines()

total_points = 0;
for line in lines:
    line_as_list = line.strip().split(' ')
    opponents_choise = line_as_list[0]
    own_choise = line_as_list[1]
    total_points += points_array[choises_dict[own_choise]][choises_dict[opponents_choise]]

print(total_points)