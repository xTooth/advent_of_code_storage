file = open('input.txt', 'r')
lines = file.readlines()

def determine_points(first: set[chr],second: set[chr] ):
    char = next(iter(first.intersection(second))) # works since rules state there can only be one such character
    char_val = ord(char)
    if  char_val > 96:      # determine if upper or lower case
        return char_val - 96  # Offset lower case
    return char_val - 38    # Offset upper case


total_points = 0;
for line in lines:
    cleaned_line = line.strip()
    first_half = cleaned_line[:len(cleaned_line)//2]
    second_half = cleaned_line[len(cleaned_line)//2:]
    total_points += determine_points(set(first_half), set(second_half))

print(total_points)