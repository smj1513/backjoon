N = int(input())
words = []
for i in range(N):
    words.append(input())
words = sorted(set(words), key=lambda x: (len(x), x))
for word in words:
    print(word)