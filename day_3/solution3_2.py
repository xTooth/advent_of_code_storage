file = open('input.txt', 'r')
lines = file.readlines()

def determine_points(first: set[chr], second: set[chr], third: set[chr]):
    char = next(iter(first.intersection(second).intersection(third)))  # works since rules state there can only be one such character
    char_val = ord(char)
    if  char_val > 96:      # determine if upper or lower case
        return char_val - 96  # Offset lower case 
    return char_val - 38    # Offset upper case


total_points = 0;
strs = []
for line in lines:
    strs.append(line.strip())
    if(len(strs) == 3):
        total_points += determine_points(set(strs[0]), set(strs[1]), set(strs[2]))
        strs = []
print(total_points)