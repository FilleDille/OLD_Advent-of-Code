import time

def part_1():
    t0 = time.time()
    with open('input.txt', 'r') as f:
        inp = f.readlines()
        f.close()

    counter = 0

    for i in range(1, len(inp)):
        if int(inp[i]) > int(inp[i - 1]):
            counter += 1

    t1 = time.time()
    print((t1-t0)*1000)

    return(counter)


def part_2():
    with open('input.txt', 'r') as f:
        inp = f.readlines()
        f.close()

    counter = 0

    for i in range(3, len(inp)):
        group_1 = int(inp[i]) + int(inp[i - 1]) + int(inp[i - 2])
        group_2 = int(inp[i - 1]) + int(inp[i - 2]) + int(inp[i - 3])
        if group_1 > group_2:
            counter += 1

    return(counter)


print(part_1())
