file = open('input.txt', 'r')
lines = file.readlines()


input = []
for line in lines:
    trees = line.strip()
    input.append(list(trees))

val = 0 
for y_cord in range(0, len(input)):
    for x_cord in range(0,len(input[0])):
        value = int(input[y_cord][x_cord])
        xe = 0
        xw = 0
        yn = 0
        ys = 0

        # check x ->
        for x in range(x_cord,len(input[0])):
            if x+1 > len(input[0])-1:
                break
            xe += 1
            if int(input[y_cord][x+1]) >= value:
                break
                
        # check x <-
        for x in range(x_cord, -1, -1):
            if x-1 < 0:
                break
            xw +=1
            if int(input[y_cord][x-1]) >= value:
                break

        # check y ->
        for y in range(y_cord,len(input)):
            if y+1 > len(input)-1:
                break
            ys += 1
            if int(input[y+1][x_cord]) >= value:
                break
                
        # check y <-
        for y in range(y_cord, -1, -1):
            if y-1 < 0:
                break
            yn +=1
            if int(input[y-1][x_cord]) >= value:
                break

        temp = xe * xw * yn * ys
        if temp > val:
            val = temp

print(val)