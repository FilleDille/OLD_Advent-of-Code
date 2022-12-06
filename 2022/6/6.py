import sys
from time import time


class elf:
    t0 = time()

    with open('input.txt', 'r') as f:
        raw = f.read()
        f.close()

    def part_1():
        for i in range(3, len(elf.raw)):
            if len(set(elf.raw[i-4:i+1])) == 4:
                return i + 1

    def part_2():
        for i in range(13, len(elf.raw)):
            if len(set(elf.raw[i-14:i+1])) == 14:
                return i + 1


if __name__ == "__main__":
    part = sys.argv[1]

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time()

    print(f'{str(round((t1-elf.t0)*1000,1))} ms för del {part}')
