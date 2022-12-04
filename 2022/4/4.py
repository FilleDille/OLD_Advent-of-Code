import sys
from time import time


class elf:
    t0 = time()

    counter = 0
    elf_1_sets = []
    elf_2_sets = []

    for line in open('input.txt', 'r'):
        n1_1, n2_1, n1_2, n2_2 = map(lambda x: int(
            x), line.strip('\n').replace('-', ',').split(','))
        elf_1_sets.append(set(range(int(n1_1), int(n2_1) + 1)))
        elf_2_sets.append(set(range(int(n1_2), int(n2_2) + 1)))

    def part_1():
        for elf_1, elf_2 in zip(elf.elf_1_sets, elf.elf_2_sets):
            if len(elf_1 - elf_2) == 0 or len(elf_2 - elf_1) == 0:
                elf.counter += 1

        return elf.counter

    def part_2():
        for elf_1, elf_2 in zip(elf.elf_1_sets, elf.elf_2_sets):
            if len(elf_1 & elf_2) > 0:
                elf.counter += 1

        return elf.counter


if __name__ == "__main__":
    part = sys.argv[1]

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time()

    print(f'{str(round((t1-elf.t0)*1000,3))} ms för del {part}')
