T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    sum_arr = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_line = 0
            for k in range(i, i+M):
                sum_line += sum(matrix[k][j:j+M])
            sum_arr.append(sum_line)
    print(f"#{tc+1}", max(sum_arr))
