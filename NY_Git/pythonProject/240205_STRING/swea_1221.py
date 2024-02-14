# import sys
# sys.stdin = open('swea_1221.py', 'r')

T = int(input())

number_dict = {
    0: 'ZRO',
    1: 'ONE',
    2: 'TWO',
    3: 'THR',
    4: 'FOR',
    5: 'FIV',
    6: 'SIX',
    7: 'SVN',
    8: 'EGT',
    9: 'NIN'
}

for tc in range(1, T+1):
    case, len = input().split()
    str_lst = list(input().split())
    num_lst = []

    # 문자열 > 숫자로 변경
    for str in str_lst:
        for key, value in number_dict.items():
            if value == str:
                num_lst.append(key)

    # 정렬하기
    num_lst.sort()

    # 숫자 > 문자열로 변경
    result = []
    for num in num_lst:
        for key, value in number_dict.items():
            if key == num:
                result.append(value)

    print(case)
    print(' '.join(result))
