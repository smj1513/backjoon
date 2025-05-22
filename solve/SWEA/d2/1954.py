T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(T):
    N = int(input())
    # 동 남 서 북
    x, y = 0, 0
    n = 1
    dr = 0
    matrix = [[0]*N]*N
    for _ in range(N*N):
        nx, ny = x+dx[dr], y+dy[dr]
        if 0 <= x < N and 0 <= y < N and matrix[x][y] == 0:
            x, y = nx, ny
            matrix[x][y] = n
            n += 1
        else:
            dr = (dr+1)%4
        matrix[x][y] = n
    print(f"#{tc+1}")
    for m in matrix:
        for a in m:
            print(a, end=" ")
        print()