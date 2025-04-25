### 나중에 다시 풀어보기

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

cnt = []
# N = 8, M = 8 일 경우에 최소 한번 실행 되어야 하기 때문에, N-7, M-7
for i in range(N-7):
    for j in range(M-7):
        index_w = 0 #흰색으로 시작
        index_b = 0 #검은색으로 시작
        for a in range(i, i+8): # 시작지점부터 8칸 보고
            for b in range(j, j+8): # 시작지점부터 8칸 보고
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        index_w += 1
                    else:
                        index_b += 1
                else:
                    if board[a][b] != 'W':
                        index_b += 1
                    else:
                        index_w += 1
        cnt.append(index_w)
        cnt.append(index_b)
print(min(cnt))




