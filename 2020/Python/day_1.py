def main():
    with open("input.txt", 'r') as f:
        raw = list(map(lambda x: int(x.replace('\n', '')), f.readlines()))
    part_2(raw)

def part_1(inp):
    for number in inp:
        missing_number = 2020 - number
        if missing_number in inp:
            prod = number * missing_number
            print(f'{number} * {missing_number} = {prod}')
            break

def part_2(inp):
    for number_1 in inp:
        missing_number_1 = 2020 - number_1
        raw_filtered = list(filter(lambda x: x <= missing_number_1, inp))

        for number_2 in raw_filtered:
            missing_number_2 = missing_number_1 - number_2

            if missing_number_2 in raw_filtered:
                prod = number_1 * number_2 * missing_number_2
                print(f'{number_1} * {number_2} * {missing_number_2} = {prod}')
                break
        else:
            continue
        break
main()