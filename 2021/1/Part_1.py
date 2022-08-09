def main():
    with open('input.txt', 'r') as f:
        inp = f.readlines()
        f.close()

    counter = 0

    for i in range(1, len(inp)):
        if int(inp[i]) > int(inp[i - 1]):
            counter += 1

    return(counter)

if __name__ == '__main__':
    print(main())