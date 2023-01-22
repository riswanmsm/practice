from sys import path

path.append('./modules')

import module

list_zeros = [0 for i in range(5)]
list_ones = [1 for i in range(5)]

print(module.sum_list(list_zeros))
print(module.prod_list(list_ones))

