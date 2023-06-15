import timeit

t0 = timeit.default_timer()

with open("input.txt", 'r') as f:
    raw = list(map(lambda x: int(x.replace('\n', '')), f.readlines()))

for number in raw:
    missing_number = 2020 - number
    if missing_number in raw:
        prod = number * missing_number
        print(f'{number} * {missing_number} = {prod}')
        break

t1 = timeit.default_timer()

print(f'Elapsed time: {round((t1-t0) * 1_000_000, 3)} µs')
