from functools import cache


file = open('input.txt', 'r')
lines = file.readlines()

numbers = [int(x) for x in lines[0].strip().split()]


@cache  # <- thank you google:
# https://www.datacamp.com/tutorial/python-cache-introduction
# this practically solves the time and size complexity of this task
# part 1 works without it, but part 2 did not seem to ever finish calculation
def recurse(stone, iteration: int, goal: int):
    # final leaf found, return 1
    if iteration == goal:
        return 1
    # handle leaf in entirety recursively
    new_stones = []
    if stone == 0:
        new_stones.append(1)
    elif len(str(stone)) % 2 == 0:
        new_stones.append(int(str(stone)[:len(str(stone)) // 2]))
        new_stones.append(int(str(stone)[len(str(stone)) // 2:]))
    else:
        new_stones.append(stone * 2024)
    return sum([recurse(x, iteration + 1, goal) for x in new_stones])


# part 1
print(sum([recurse(number, 0, 25) for number in numbers]))
# part 2
print(sum([recurse(number, 0, 75) for number in numbers]))
