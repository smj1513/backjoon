result = []
for _ in range(10):
    window_size = int(input())
    matrix = []
    cnt = 0
    for i in range(8):
        matrix.append(list(input()))
    for i in range(len(matrix)):
        for j in range(len(matrix)-window_size+1):
            # 가로 회문
            sub_str = matrix[i]
            sb_str = sub_str[j:(j + window_size)]
            if sb_str == sb_str[::-1]:
                cnt += 1
            else:
                continue
    mat_t = list(map(list, zip(*matrix)))

    for i in range(len(mat_t)):
        for j in range(len(mat_t)-window_size+1):
            sb_str = mat_t[i][j:j+window_size]
            if sb_str == sb_str[::-1]:
                cnt += 1
            else:
                continue
    result.append(cnt)
for i in range(len(result)):
    print(f"{i+1}", result[i])