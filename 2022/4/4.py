import sys
from time import time


class elf:
    t0 = time()

    with open('input.txt', 'r') as f:
        raw = f.read().splitlines()
        f.close()

    def part_1():
        counter = 0

        for line in elf.raw:
            elf_1_raw = line.split(',')[0]
            n1_1 = elf_1_raw.split('-')[0]
            n2_1 = elf_1_raw.split('-')[1]

            elf_2_raw = line.split(',')[1]
            n1_2 = elf_2_raw.split('-')[0]
            n2_2 = elf_2_raw.split('-')[1]

            elf_1 = set(range(int(n1_1), int(n2_1) + 1))
            elf_2 = set(range(int(n1_2), int(n2_2) + 1))

            if len(elf_1 - elf_2) == 0 or len(elf_2 - elf_1) == 0:
                counter += 1

        return counter

    def part_2():
        pass


if __name__ == "__main__":
    part = sys.argv[1]

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time()

    print(f'{str(round((t1-elf.t0)*1000,3))} ms för del {part}')
