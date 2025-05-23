T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(str, input().split())) for _ in range(N)]
    matrix_t = list(map(list, zip(*matrix)))
    cnt = 0
    for line1, line2 in zip(matrix, matrix_t):
        cnt += ''.join(line1).split("0").count('1'*K)
        cnt += ''.join(line2).split("0").count('1'*K)
    print(f"#{tc+1}",cnt)