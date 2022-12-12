import sys
from time import time
import numpy as np


class elf:
    t0 = time()

    with open('input.txt', 'r') as f:
        inp = f.read().splitlines()
        f.close()

    tree_list = []
    letters = []

    for line in inp:
        letters.clear()
        for letter in line:
            letters.append(letter)
        tree_list.append(list(letters))

    tree_array = np.array(tree_list)

    width = len(tree_array[0, :])
    height = len(tree_array[:, 0])

    def part_1():
        visible_trees = elf.height * 2 + (elf.width - 2) * 2

        for y in range(1, elf.height - 1):
            for x in range(1, elf.width - 1):
                current_tree = elf.tree_array[y, x:x + 1][0]
                trees_right = elf.tree_array[y, x + 1:elf.width]
                trees_left = elf.tree_array[y, 0:x]
                trees_above = elf.tree_array[:y, x]
                trees_below = elf.tree_array[y + 1:, x]

                if current_tree > min([max(trees_above), max(trees_below), max(trees_left), max(trees_right)]):
                    visible_trees += 1

        return visible_trees

    def part_2():

        visible_trees_right = 0
        visible_trees_left = 0
        visible_trees_above = 0
        visible_trees_below = 0
        scenic_score = []

        for y in range(1, elf.height - 1):
            for x in range(1, elf.width - 1):
                visible_trees_right = 0
                visible_trees_left = 0
                visible_trees_above = 0
                visible_trees_below = 0

                current_tree = elf.tree_array[y, x:x + 1][0]
                trees_right = elf.tree_array[y, x + 1:elf.width]
                trees_left = elf.tree_array[y, 0:x]
                trees_above = elf.tree_array[:y, x]
                trees_below = elf.tree_array[y + 1:, x]

                counting = True

                for tree in trees_right:
                    if counting == True:
                        if current_tree > tree:
                            visible_trees_right += 1
                        elif current_tree == tree:
                            visible_trees_right += 1
                            counting = False
                        else:
                            visible_trees_right += 1
                            counting = False

                counting = True

                for tree in reversed(trees_left):
                    if counting == True:
                        if current_tree > tree:
                            visible_trees_left += 1
                        elif current_tree == tree:
                            visible_trees_left += 1
                            counting = False
                        else:
                            visible_trees_left += 1
                            counting = False

                counting = True

                for tree in reversed(trees_above):
                    if counting == True:
                        if current_tree > tree:
                            visible_trees_above += 1
                        elif current_tree == tree:
                            visible_trees_above += 1
                            counting = False
                        else:
                            visible_trees_above += 1
                            counting = False

                counting = True

                for tree in trees_below:
                    if counting == True:
                        if current_tree > tree:
                            visible_trees_below += 1
                        elif current_tree == tree:
                            visible_trees_below += 1
                            counting = False
                        else:
                            visible_trees_below += 1
                            counting = False

                temp_score = visible_trees_right * visible_trees_left * \
                    visible_trees_above * visible_trees_below
                scenic_score.append(temp_score)

        return max(scenic_score)


if __name__ == "__main__":
    part = sys.argv[1]

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time()

    print(f'{str(round((t1-elf.t0)*1000,1))} ms för del {part}')
