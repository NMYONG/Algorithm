import copy
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    temp_arr = copy.deepcopy(arr)
    print(arr)
    print(temp_arr)
    temp_arr[1][1] = 0
    print(arr)
    print(temp_arr)
    temp_arr = copy.deepcopy(arr)
    print(arr)
    print(temp_arr)
