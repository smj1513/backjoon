import sys
read = sys.stdin.readline
N = int(read())
data = sorted([tuple(map(int, read().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))
for d in data:
    print(*d)