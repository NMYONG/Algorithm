# num = 5
# binV = bin(num)
# hexV = hex(num)
# print(num)
# print(num, binV, type(binV))
# print(num, hexV, type(hexV))


def bitPrint(num):
    for j in range(4):
        if num & 1 << j:  # 1 << 0
            print(1)
        else:
            print(0)

bitPrint(5)
print(bin(5))
    #
    # # 0번째
    # if num & 1: # 1 << 0
    #     print(1)
    # else:
    #     print(0)
    # # 1번쨰
    # if num & 2: # 1 << 1
    #     print(1)
    # else:
    #     print(0)
    # # 2번째
    # if num & 4: # 1 <<2
    #     print(1)
    # else:
    #     print(0)


def decToBin(num):
    s = ''
    for j in range(3, -1, -1):
        s += '1' if num & 1 << j else '0'
        # if num & 1 <<j:
        #     s += '1'
        # else:
        #     s += '10'
    return s

# 16진수 값 하나를 2진수 4자의 문자열로 변환
def hexTobin(num):

    num = int(num, 16)

    s = ''
    for j in range(3, -1, -1):
        s += '1' if num & 1 << j else '0'

    return s