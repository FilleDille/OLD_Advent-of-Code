def part_1():
    with open('input.txt', 'r') as f:
        input_raw = f.readlines()
        f.close()

    temp_right = []
    counter = 0

    for ln in input_raw:
        temp_right = ln.split(' | ')[1].split(' ')
        temp_right[3] = temp_right[3].replace('\n','')

        for digit in temp_right:
            print(len(digit))
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                counter += 1
        
    return counter

print(part_1())