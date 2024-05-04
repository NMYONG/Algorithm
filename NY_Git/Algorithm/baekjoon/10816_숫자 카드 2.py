import sys
input = sys.stdin.readline

N = int(input())
hasCard = list(map(int, input().split()))
M = int(input())
checkCard = list(map(int, input().split()))

dic = {}
for card in hasCard:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

for card in checkCard:
    if card in dic:
        print(dic[card], end=' ')
    else:
        print(0, end=' ')



