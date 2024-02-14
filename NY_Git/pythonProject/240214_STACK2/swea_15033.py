T = int(input())

for tc in range(1, T+1):
    N = int(input())

def getWinner(w1, w2):
    pass

def game(i, j):
    if i == j:# 종료조건
        return i

    winner1 = game(i, (i+j)//2)
    winner2 = game((i+j)//2+1, j)
    return getWinner(winner1, winner2)


N = int(input())
s = list(map(int, input().split()))

game(0, N-1)