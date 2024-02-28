# 내 코드
time = [15, 30, 50, 10]
time.sort()

t = 0
while len(time):
    t += time.pop(0) * len(time)

print(t)



# 강사님 코드
person = [15, 30, 50, 10]
n = len(person)
person.sort()
sum = 0
left_person = n - 1

for turn in range(n):
    time = person[turn]
    sum += left_person * time
    left_person -= 1

print(sum)





# Fractional Knapsack
n = 3
target = 30
things = [(5, 50), (10, 60), (20, 140)]

things.sort(key=lambda x : (x[1]/x[0]), reverse=True) # kg당 가격으로 내림차순 정렬

sum = 0

for kg, price in things:
    per_price = price / kg
    # 가방에 남은 용량이 얼마 되지 않는다면, 물건을 잘라 가방에 넣고 끝냄
    if target < kg:
        sum += target * per_price
        break

    sum += price
    target -= kg

print(int(sum))
