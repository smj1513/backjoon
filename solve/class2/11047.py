import sys
read = sys.stdin.readline
N, K = map(int, read().split())
coins = [int(read().strip()) for _ in range(N)]
cnt = 0
while K > 0:
    filtered = [c for c in coins if c <= K]
    max = filtered[-1] # 정렬되어 들어오기 때문
    coin_cnt = K//max
    cnt += coin_cnt
    K -= coin_cnt*max
print(cnt)