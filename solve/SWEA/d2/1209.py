result = []
for _ in range(10):
    T = int(input())
    matrix = []
    for i in range(100):
        matrix.append(list(map(int, input().split())))
    row_sum = []
    col_sum = []
    cross_sum = 0
    rev_cross_sum = 0
    for i in range(0, len(matrix)):
        row_sum.append(sum(matrix[i]))
        col_sum_value = 0
        for j in range(0, len(matrix)):
            col_sum_value += matrix[j][i]
            if i == j :
                cross_sum += matrix[i][j]
            if (99 - i) == j :
                rev_cross_sum += matrix[i][j]
        col_sum.append(col_sum_value)
    result.append(max(max(row_sum), max(col_sum), cross_sum, rev_cross_sum))

for i in range(10):
    print(f"#{i+1}", result[i])