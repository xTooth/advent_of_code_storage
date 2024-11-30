visited = set()
board = []
queue = []

def bfs(board: list[list[chr]]):
    while(queue):
        current = queue.pop(0)
        y, x = current['pos']
        current_char = board[y][x] if board[y][x] != 'S' else 'a'
        if board[y][x] == 'a':
            return current['visited']
        current['visited'] += 1
        current_char_as_int = ord(current_char)
        if (y > 0 and current_char_as_int - ord(board[y-1][x]) <= 1 and (y-1, x) not in visited):
            queue.append(
                {
                'pos': (y-1, x),
                'visited': current['visited']
                }
            )
            visited.add((y-1, x))

        if (y < len(board)-1 and current_char_as_int - ord(board[y+1][x]) <= 1 and (y+1, x) not in visited):
            queue.append(
                {
                'pos': (y+1, x),
                'visited': current['visited']
                }
            )
            
            visited.add((y+1, x))

        if (x > 0 and current_char_as_int - ord(board[y][x-1]) <= 1 and (y, x-1) not in visited):
            queue.append(
                {
                'pos': (y, x-1),
                'visited': current['visited']
                }
            )
            visited.add((y, x-1))

        if (x < len(board[0])-1 and current_char_as_int - ord(board[y][x+1]) <= 1 and (y, x+1) not in visited):
            queue.append(
                {
                'pos': (y, x+1),
                'visited': current['visited']
                }
            )
            visited.add((y, x+1))
        

file = open('input.txt', 'r')
lines = file.readlines()
for line in lines:
        board.append(list(line.strip()) ) 

goal = (0,0)
for y in range(0,len(board)):
    for x in range(0,len(board[0])):
        if board[y][x] == 'E':
            queue.append(
                {
                'pos': (y, x),
                'visited': 0
                }
            )
            board[y][x] = 'z'
            
        if board[y][x] == 'S':
            board[y][x] = 'a'
print(bfs(board))
   
