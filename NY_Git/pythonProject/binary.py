# 16진수 <=> 2진수 <=> 10진수

# 10진수 > 2진수
def decToBin(decimal):
    result = []

    while decimal:
        result.append(decimal % 2)
        decimal //= 2

    return list(reversed(result))
print(decToBin(35))


# 2진수 > 10진수
def binToDec(binary):
    result = 0
    for i in binary:
        result = result*2 + int(i)
    return result
print(binToDec('100011'))


# 16진수 > 2진수
def hexToBin(hexadecimal):
    mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    result = ''
    for i in hexadecimal:
        result += mapping[i]
    return result
print(hexToBin('23'))


# 2진수 > 16진수
def binToHex(binary):
    mapping = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
               '0100': '4', '0101': '5', '0110': '6', '0111': '7',
               '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
               '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    result = ''
    for i in range(0, len(binary), 4):
        bin_chunk = binary[i:i+4]
        result += mapping[bin_chunk]
    return result
print(binToHex('00100011'))