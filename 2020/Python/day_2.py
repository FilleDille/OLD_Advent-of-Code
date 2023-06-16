def main():
    with open("input_2.txt", 'r') as f:
        raw = list(map(lambda x: x.replace('\n', ''), f.readlines()))
    part_1(raw)

def part_1(inp):
    counter = 0

    for line in inp:
        parts = line.split(" ")
        rng = parts[0]
        char = parts[1][0]
        substr = parts[2]
        char_counter = 0

        for c in substr:
            if c == char:
                char_counter += 1

        if int(rng.split('-')[0]) <= char_counter <= int(rng.split('-')[1]):
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
