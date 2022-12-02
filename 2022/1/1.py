import sys


class elf:
    elf_list = []
    current_elf = 0

    with open('input.txt', 'r') as f:
        raw = f.readlines()
        f.close()

    for _ in raw:
        if _ == '\n':
            elf_list.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(_.replace('\n', ''))

    elf_list.sort(reverse=True)

    def part_1():
        return elf.elf_list[0]

    def part_2():
        return sum(elf.elf_list[:3])


if __name__ == "__main__":
    part = sys.argv[1].lower()

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
