def f2(n):
    n *= 2
    print(n)

def f1(c, d):
    e = c + d
    f2(e)

a = 10
b = 20
c = a + b
f1(a, b)




# 강사님 설명
# Function call
def fun2(x):
    x *= 2
    print('fun2:', x)

def fun1(x):
    x += 1
    if x == 5:
        return
    print('fun1:', x)
    fun1(x)

for i in range(1, 5):
    print('main:', i)
    fun1(i)