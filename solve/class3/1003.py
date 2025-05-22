import sys
read = sys.stdin.readline
N = int(read())
for _ in range(N):
    n = int(read())
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    if n > 1:
        for j in range(n-1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2]+cnt_1[-1])
    print(cnt_0[n], cnt_1[n])