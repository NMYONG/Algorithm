# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             for l in range(1, 4):
#                 print(1000*i + 100*j + 10*k + l)


# def KFC(x):
#     print(x)
#     x += 1
#     print(x)
#
# x = 3
# KFC(x + 1)
# print(x)


# def BBQ(x):
#     x += 10
#     print(x)
#
# def KFC(x):
#     print(x)
#     x += 3
#     BBQ(x+2)
#     print(x)
#
# x = 3
# KFC(x+1)
# print(x)


# def KFC(x):
#     if x ==2:
#         return
#     print(x)
#     KFC(x+1)
#     print(x)
#
# KFC(0)
# print('끝')


# def function(x):
#
#     if x == 6:
#         return
#     print(x, end= ' ')
#     function(x+1)
#     print(x, end= ' ')
#
# function(0)


# def function(x):
#     if x == 3:
#         return
#
#     for i in range(2):
#         function(x+1)
#
# function(0)


# path = []
#
# def KFC(x):
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(3):
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#
# KFC(0)


# path = []
#
# def function(x):
#     if x == 4: # level = 3
#         print(path)
#         return
#
#     for i in range(1, 7): # branch = 6
#         path.append(i)
#         function(x+1)
#         path.pop()
#
# function(1)


# path = []
# def function(x):
#     if x == 5: # level = 4
#         print(path)
#         return
#
#     for i in range(1, 5): # branch = 4
#         path.append(i)
#         function(x+1)
#         path.pop()
#
# function(1)


# # 중복 순열
# path = []
# def Type1(x):
#     if x == N:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         Type1(x+1)
#         path.pop()
#
# 중복을 제거한 순열
path = []
used = [False for _ in range(7)]
def Type2(x):
    if x == 3:
        print(path)
        return

    for i in range(1, 7):
        if used[i] == True : continue
        used[i] = True
        path.append(i)
        Type2(x+1)
        path.pop()
        used[i] = False
#
#
# N, type = map(int, input().split())
#
# if type == 1:
#     Type1(0)
# if type == 2:
#     Type2(2)


# 완전탐색
path = []
cnt = 0

def kfc(x, sum):
    global cnt

    if sum > 10:
        return

    if x == 3:
        # print(f'{path} = {sum}')
        cnt += 1
        return

    for i in range(1, 7):
        path.append(i)
        kfc(x+1, sum+i)
        path.pop()

kfc(0, 0)
print(cnt)