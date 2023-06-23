import numpy as np

with open('input_3.txt', 'r') as f:
    inp = f.read().splitlines()
    f.close()


map_list = []

for line in inp:
    map_list.append(list(line))

map_array = np.array(map_list)
map_array_height = len(map_array)
map_array_width = len(map_array[0])
mask_tree = map_array == '#'
index_array = np.array([(x * 3) % map_array_width for x in np.arange(map_array_height)])
mask_path = np.zeros_like(mask_tree, dtype=bool)
mask_path[np.arange(mask_path.shape[0]), index_array] = True
mask_final = mask_tree & mask_path

print(np.count_nonzero(mask_final))