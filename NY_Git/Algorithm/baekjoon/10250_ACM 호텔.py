# T = int(input())
# for tc in range(1, T+1):
#     H, W, N = map(int, input().split())
#
#     YY = 1
#     XX = 0
#
#     for i in range(1, N+1):
#         if XX > H:
#             XX = 1
#             YY += 1
#         else:
#             XX += 1
#
#     print(YY, XX)

T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())

    floor = n % h
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1

    print(floor * 100 + room_line)