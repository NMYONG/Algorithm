# import sys
# sys.stdin = open("240130/1209.txt", "r")

# min 함수
def my_min(lst):
    min_value = 1e10
    min_index = 0
    for i in range(len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = i
    return min_value, min_index

# max 함수
def my_max(lst):
    max_value = 0
    max_index = 0
    for i in range(len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i
    return max_value, max_index

for test_case in range(1, 11):
    dump = int(input())
    dump_lst = list(map(int, input().split()))

    for i in range(dump):
        dump_max, max_index = my_max(dump_lst)
        dump_min, min_index = my_min(dump_lst)

        dump_lst[max_index] -= 1
        dump_lst[min_index] += 1

        dump_max, max_index = my_max(dump_lst)
        dump_min, min_index = my_min(dump_lst)

        if dump_lst[max_index] - dump_lst[min_index] <= 1:
            break

    result = dump_max - dump_min

    print(f'#{test_case} {result}')