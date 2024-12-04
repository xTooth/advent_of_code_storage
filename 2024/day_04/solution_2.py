file = open('input.txt', 'r')
lines = file.readlines()


def find_word_in_direction(
    board,
    grid_height,
    grid_width,
    word_to_find,
    index,
    list,
    char,
    direction_x,
    direction_y
):
    if index == len(word_to_find):
        return True

    if (
        0 <= char < grid_width
        and 0 <= list < grid_height
        and word_to_find[index] == board[list][char]
    ):
        return find_word_in_direction(
            board,
            grid_height,
            grid_width,
            word_to_find,
            index + 1,
            list + direction_y,
            char + direction_x,
            direction_x,
            direction_y
        )

    return False


# create twodimensional array
board = []
for line in lines:
    board.append([x for x in line])

word_to_find = 'MAS'

grid_width = len(board[0]) - 1  # /n is a character
grid_height = len(board)
ans = 0

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

for list in range(0, grid_height):
    for char in range(0, grid_width):
        if board[list][char] == word_to_find[1]:
            if 0 < list < grid_height and 0 < char < grid_width:
                if (find_word_in_direction(
                    board,
                    grid_height,
                    grid_width,
                    word_to_find,
                    0,
                    list-1,
                    char-1,
                    1,
                    1
                ) or find_word_in_direction(
                    board,
                    grid_height,
                    grid_width,
                    word_to_find,
                    0,
                    list+1,
                    char+1,
                    -1,
                    -1
                )) and (find_word_in_direction(
                    board,
                    grid_height,
                    grid_width,
                    word_to_find,
                    0,
                    list-1,
                    char+1,
                    -1,
                    1
                ) or find_word_in_direction(
                    board,
                    grid_height,
                    grid_width,
                    word_to_find,
                    0,
                    list+1,
                    char-1,
                    1,
                    -1
                )):
                    ans += 1

print(ans)
