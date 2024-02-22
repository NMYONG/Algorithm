# 7글자씩 잘라서 10진수로 변환

def binToDec(s):
    result = 0
    for c in s:
        result = result*2 + int(c)
    return result

s = '0000000111100000011000000111100110000110000111100111100111111001100111'
l = len(s)

for c in range(0, len(s), 7):
    print(binToDec(s[c:c+7]), end=' ')