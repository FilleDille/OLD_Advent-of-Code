import sys
import re
import time


class elf:
    item_list = []

    with open('input.txt', 'r') as f:
        inp = f.read().splitlines()
        f.close()

    for backpack in inp:
        compartment_1 = backpack[:int(len(backpack)/2)]
        compartment_2 = backpack[int(len(backpack)/2):]

        item_list.append((set(compartment_1) & set(compartment_2)).pop())

    def part_1():
        ucase_letters = list(filter(lambda x: 64 < ord(x) < 97, elf.item_list))
        ucase_values = list(map(lambda x: ord(x)-38, ucase_letters))
        lcase_letters = list(
            filter(lambda x: 96 < ord(x) < 123, elf.item_list))
        lcase_values = list(map(lambda x: ord(x)-96, lcase_letters))

        return sum(ucase_values) + sum(lcase_values)

    def part_2():
        pass


if __name__ == "__main__":
    t0 = time.time()
    part = sys.argv[1]

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time.time()

    print(f'{str(round((t1-t0)*1000,3))} ms för del {part}')
