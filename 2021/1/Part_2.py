def main():
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

if __name__ == '__main__':
    print(main())