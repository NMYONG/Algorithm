A, B, V = map(int, input().split())
# day = 0
# state = 0
# while True:
#     day += 1
#
#     state += A
#     if state >= V:
#         break
#     state -= B
#
# print(day)

# 올라갈 수 있는 거리 = A
# 미끄러지는 거리 = B
# 하루에 갈 수 있는 거리 = A - B
# 올라가야 할 거리 = V - B
if (V - B) % (A - B) == 0: # 나머지가 0이면 낮 동안에 정상까지 갔다는 뜻
    print((V - B) // (A - B))
else: # 밤에 미끄러졌다는 뜻
    print((V - B) // (A - B) + 1)