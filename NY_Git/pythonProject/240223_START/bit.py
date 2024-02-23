# print(bin(10))
# print(hex(10))
# print()
# print(int('1011', 2))
# print(int('b', 16))
# print()
# # 0b11011110 & 0b11011
# print(bin(int('11011110', 2) & int('11011', 2)))
# print(0b11011110 & 0b11011)
# # 0x4A3 | 25
# print(int('4A3', 16) | 25)
# print(0x4A3 | 25)
# print()
# # 어떤 값이던 임의의 수로 2회 XOR 하면 원래 수로 돌아온다
# print(7070 ^ 1004)
# print((7070 ^ 1004) ^ 1004)
# print()
# # 수를 입력받고 암호화, 복호화 하는 프로그램 제작, KEY = 1004
# KEY = 1004
# def encoding_decoding(num):
#     return num ^ 1004
#
# print(encoding_decoding(1000))
# print(encoding_decoding(encoding_decoding(1000)))
# print()
#
# # 비트연산(<<)
# t = 1
# for i in range(5):
#     print(bin(t), t)
#     t = t << 1
# print()
# # 2의 보수
# # MSB(2진수에서 가장 높은 자리수)가 1이면 음수, 0이면 양수

# # ~연산자
# N, M = 5, 31
#
# def test():
#     tar = M
#     for i in range(N):
#         if tar & 0x1 == 0:
#             return False
#         tar = tar >> 1
#     return True
#
# print(test())

# 실수
print(f'{0.1 : .100f}')