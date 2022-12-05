import sys
from time import time
import queue


class elf:
    t0 = time()

    with open('input_init.txt', 'r') as f:
        raw_init = f.read().splitlines()
        f.close()

    stack_dict = {}

    for i in range(1, 10):
        stack_dict[i] = queue.LifoQueue()

    for line in reversed(raw_init):
        for i in range(35):
            if line[i].isalpha():
                stack_dict[int((i - (i % 4))/4)+1].put(line[i])

    with open('input_instructions.txt', 'r') as f:
        raw_instr = f.read().splitlines()
        f.close()

    def part_1():
        for line in elf.raw_instr:
            instr_number, instr_from, instr_to = map(lambda x: int(x), line.replace(
                'move ', '').replace('from ', '').replace('to ', '').split())

            for i in range(instr_number):
                elf.stack_dict[instr_to].put(elf.stack_dict[instr_from].get())

        top_crates = ''

        for i in range(1, 10):
            top_crates = ''.join((top_crates, elf.stack_dict[i].get()))

        return top_crates

    def part_2():
        crane_9001 = queue.LifoQueue()

        for line in elf.raw_instr:
            instr_number, instr_from, instr_to = map(lambda x: int(x), line.replace(
                'move ', '').replace('from ', '').replace('to ', '').split())

            for i in range(instr_number):
                crane_9001.put(elf.stack_dict[instr_from].get())

            for i in range(instr_number):
                elf.stack_dict[instr_to].put(crane_9001.get())

        top_crates = ''

        for i in range(1, 10):
            top_crates = ''.join((top_crates, elf.stack_dict[i].get()))

        return top_crates


if __name__ == "__main__":
    part = sys.argv[1]

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time()

    print(f'{str(round((t1-elf.t0)*1000,1))} ms för del {part}')
