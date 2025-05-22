import sys
read = sys.stdin.readline
N =  int(read())
times = list(map(int, read().split()))
times.sort()
time = 0
sum = 0
for t in times:
    time += t
    sum += time
print(sum)