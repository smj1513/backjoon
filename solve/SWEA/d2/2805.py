T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(N)]
    sum = 0
    h = N // 2
    for i in range(len(matrix)):
        if i <= h: #위 삼각형
            for j in range(h-i, h+i+1):
                sum += matrix[i][j]
        else: # 아래 삼각형
            for j in range(i-h, N+h-i):
                sum += matrix[i][j]
    print(f"#{tc+1}", sum)