result = []
for _ in range(10):
    size = int(input())
    matrix = []
    for i in range(size):
        matrix.append(list(map(int, input().split())))
    mat_t = list(map(list, zip(*matrix)))
    cnt = 0
    for row in mat_t:
        prev = 0
        for col in row:
            if col: # 0이 아닐때 // 0인 경우는 패스
                if col == 2 and prev == 1: #현재 s 극일때 앞이 n극일 경우 교착 상태
                    cnt += 1
                prev = col
    result.append(cnt)
for i in range(10):
    print(f"#{i+1}", result[i])