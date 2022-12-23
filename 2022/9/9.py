import sys
from time import time


class Point:

    def __init__(self):
        self.points = 1

    def add(self):
        self.points += 1


class elf:
    t0 = time()

    with open('input.txt', 'r') as f:
        inp = f.read().splitlines()
        f.close()

    x = 0
    y = 0
    h_x = 0
    h_y = 0

    point_dict = {(x, y): Point()}

    for row in inp:
        steps = int(row.split()[1])
        direction = row.split()[0]

        for i in range(steps):
            move_made = False

            if direction == 'R':
                h_x += 1
            if direction == 'L':
                h_x -= 1
            if direction == 'U':
                h_y += 1
            if direction == 'D':
                h_y -= 1

            delta = (h_x - x, h_y - y)

            if delta.count(0) == 1:  # not diagonal
                if sum(delta) in (2, -2):
                    if delta.index(0) == 1:  # change in x
                        if delta[0] == -2:
                            x -= 1
                        else:
                            x += 1
                    else:
                        if delta[1] == -2:
                            y -= 1
                        else:
                            y += 1

                    move_made = True
            else:  # diagonal, delta.count(0) == 0
                if sum(delta) == 3:  # NE
                    x += 1
                    y += 1
                elif sum(delta) == -3:  # SW
                    x -= 1
                    y -= 1
                elif sum(delta) in (1, -1):  # NW/SE
                    if delta.index(max(delta)) == 0:  # SE
                        x += 1
                        y -= 1
                    else:  # NW
                        x -= 1
                        y += 1

                move_made = True

            if move_made:
                if (x, y) in point_dict:
                    point_dict[(x, y)].add()
                else:
                    point_dict[(x, y)] = Point()

    def part_1():
        return len(elf.point_dict)

    def part_2():
        pass


if __name__ == "__main__":
    part = sys.argv[1]

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time()

    print(f'{str(round((t1-elf.t0)*1000,1))} ms för del {part}')
