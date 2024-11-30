
def _move_crate(
    from_index: int,
    to_index: int,
    stacks: list[list[chr]],
    crate:int
):
    stacks[to_index].append(stacks[from_index].pop(crate))
    return stacks


def _move_crates(
    from_index: int,
    to_index: int,
    amount: int,
    stacks: list[list[chr]]
):
    for i in range(0,amount):
        stacks = _move_crate(
            from_index=from_index,
            to_index=to_index,
            stacks=stacks,
            crate= -amount+i
        )
    return stacks


def print_chars(stacks: list[list[chr]]):
    str = ''
    for stack in stacks:
        str += stack.pop()
    print(str)

# Dirty solution as I didnt feel like actually parsing this out of the file
stacks = [
    ['H', 'T', 'Z', 'D'],  #1
    ['Q', 'R', 'W', 'T', 'G', 'C', 'S'],  #2
    ['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H'],  #3
    ['L', 'C', 'N', 'F', 'H', 'Z'],  #4
    ['G', 'L', 'F', 'Q', 'S'],  #5
    ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S'],  #6
    ['Z', 'F', 'J'],  #7
    ['D', 'L', 'V', 'Z', 'R', 'H', 'Q'],  #8
    ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D']   #9
]

file = open('input.txt', 'r')
lines = file.readlines()


for line in lines[10:]:  # input starts at line 11
    values = line.strip().split(' ')
    stacks = _move_crates(
        from_index=int(values[3])-1, # account for indexing
        to_index=int(values[-1])-1, # account for indexing
        amount=int(values[1]),
        stacks=stacks
        )
print_chars(stacks=stacks)