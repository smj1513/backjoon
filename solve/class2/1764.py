import sys
read = sys.stdin.readline
N, M = map(int, read().split())
dj = set()
bj = set()
for i in range(N):
    dj.add(read().strip())
for i in range(M):
    bj.add(read().strip())
dbj = dj.intersection(bj)

print(len(dbj))
for d in sorted(dbj):
    print(d)