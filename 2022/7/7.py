import sys
from time import time
from functools import reduce


class elfFile:

    def __init__(self, size, name):
        self.size = size
        self.name = name
        pass


class elfFolder:

    def __init__(self, name, parent):
        self.content = {}
        self.name = name
        self.parent = parent

    def add_content(self, name, content):
        self.content[name] = content

    def get_size(self, all_dir_sizes):
        files = list(filter(lambda x: isinstance(
            x, elfFile), self.content.values()))
        dirs = list(filter(lambda x: isinstance(
            x, elfFolder), self.content.values()))

        file_sizes = reduce(lambda x, y: x + int(y.size), files, 0)
        dir_sizes = reduce(lambda x, y: x + y.get_size(all_dir_sizes), dirs, 0)

        total_size = file_sizes + dir_sizes

        all_dir_sizes.append(total_size)

        return total_size


class elf:
    t0 = time()

    with open('input.txt', 'r') as f:
        terminal_log = f.read().splitlines()
        f.close()

    root = elfFolder('/', None)
    current_directory = root

    for line in terminal_log:
        split_line = line.split()

        if split_line[0] == '$':
            if split_line[1] == 'cd':
                folder = split_line[2]

                if folder == '..':
                    current_directory = current_directory.parent
                elif folder == '/':
                    current_directory = root
                else:
                    current_directory = current_directory.content[folder]
        else:
            if split_line[0] == 'dir':
                temp_dir = elfFolder(split_line[1], current_directory)
                current_directory.add_content(temp_dir.name, temp_dir)
            elif split_line[0].isnumeric():
                temp_file = elfFile(split_line[0], split_line[1])
                current_directory.add_content(temp_file.name, temp_file)

    all_dir_sizes = []
    root.get_size(all_dir_sizes)

    def part_1():
        return sum(filter(lambda x: x < 100000, elf.all_dir_sizes))

    def part_2():
        return min(list(filter(lambda x: x >= 30000000 - (70000000 - max(elf.all_dir_sizes)), elf.all_dir_sizes)))


if __name__ == "__main__":
    part = sys.argv[1]

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time()

    print(f'{str(round((t1-elf.t0)*1000,1))} ms för del {part}')
