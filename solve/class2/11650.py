import sys
input=sys.stdin.readline
N = int(input())
lis = []
for i in range(N):
    x, y = map(int, input().split())
    lis.append({'x':x, 'y':y})

lis.sort(key = lambda x:(x['x'], x['y']))
for li in lis:
    print(li['x'], li['y'])