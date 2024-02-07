# import sys
# sys.stdin = open('swea_1234.py', 'r')

for tc in range(1, 11):
    l, m = input().split()
    m_lst = [j for j in str(m)]

    i = 0
    while i < len(m_lst)-1:
        if m_lst[i] == m_lst[i+1]:
            m_lst.pop(i)
            m_lst.pop(i)
            i = max(0, i-1)
        else:
            i += 1

    result = ''.join(map(str, m_lst))
    print(f'#{tc} {result}')

