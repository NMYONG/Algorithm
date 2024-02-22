import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


n, m = map(int, input().split())

print(n+m, n*m)

