def solve(numlegs, numheads):
    for numchicks in range(0, numheads + 1):
        numrabbits = numheads - numchicks
        totlegs = 4 * numrabbits + 2 * numchicks
        if totlegs == numlegs:
            return [numrabbits, numchicks]
    return [None, None]


if __name__ == "__main__":
    heads = int(input())
    legs = int(input())
    rabbits, chickens = solve(legs, heads)

    if rabbits is None:
        print('there is no sol')
    else:
        print('no of rabbits', rabbits)
        print('no of chicken', chickens)

# output
# 35
# 94
# no of rabbits 12
# no of chicken 23
