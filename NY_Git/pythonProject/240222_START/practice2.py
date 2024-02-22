def hexToBin(hexS):
    mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    s = ''
    for c in hexS:
        s += mapping[c]
    return s

def binToDec(s):
    result = 0
    for c in s:
        result = result*2 + int(c)
    return result

s = input()
s_bin = hexToBin(s)

for c in range(0, len(s_bin), 7):
    print(binToDec(s_bin[c:c+7]), end=' ')