import sys
import pandas as pd
import time


class elf:
    score_hand_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    score_outcome_dict = {
        'win': 6,
        'draw': 3,
        'loss': 0
    }

    outcome_dict = {
        ('X', 'A'): 'draw',
        ('X', 'B'): 'loss',
        ('X', 'C'): 'win',
        ('Y', 'A'): 'win',
        ('Y', 'B'): 'draw',
        ('Y', 'C'): 'loss',
        ('Z', 'A'): 'loss',
        ('Z', 'B'): 'win',
        ('Z', 'C'): 'draw'
    }

    map_dict = {
        ('X', 'A'): 'Z',
        ('X', 'B'): 'X',
        ('X', 'C'): 'Y',
        ('Y', 'A'): 'X',
        ('Y', 'B'): 'Y',
        ('Y', 'C'): 'Z',
        ('Z', 'A'): 'Y',
        ('Z', 'B'): 'Z',
        ('Z', 'C'): 'X'
    }

    df = pd.read_csv('input.txt', header=None, sep=' ',
                     names=['opponent', 'own'])

    def part_1():
        elf.df['outcome'] = elf.df.apply(
            lambda x: elf.outcome_dict[(x['own'], x['opponent'])], axis=1)
        elf.df['points'] = elf.df.apply(
            lambda x: elf.score_outcome_dict[x['outcome']] + elf.score_hand_dict[x['own']], axis=1)

        return elf. df['points'].sum()

    def part_2():
        elf.df['own'] = elf.df.apply(
            lambda x: elf.map_dict[(x['own'], x['opponent'])], axis=1)
        elf.df['outcome'] = elf.df.apply(
            lambda x: elf.outcome_dict[(x['own'], x['opponent'])], axis=1)
        elf.df['points'] = elf.df.apply(
            lambda x: elf.score_outcome_dict[x['outcome']] + elf.score_hand_dict[x['own']], axis=1)

        return elf. df['points'].sum()


if __name__ == "__main__":
    t0 = time.time()
    part = sys.argv[1].lower()

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time.time()

    print(t1-t0)
