from itertools import combinations

num_lst = [1, 2, 3, 4, 5, 6]
op_lst = ['+', '+', '-', '*', '/']

print(list(combinations(op_lst, 3)))