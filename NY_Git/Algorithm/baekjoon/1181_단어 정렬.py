N = int(input())

wordsList = []
for n in range(N):
    wordsList.append(input())

wordsList = sorted(set(wordsList), key=lambda x: (len(x), x))

for i in wordsList:
    print(i)
