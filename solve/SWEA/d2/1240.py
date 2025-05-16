N = int(input())
for i in range(N):
    N, M = map(int, input().split())
    mat = []
    code = []
    for j in range(N):
        mat.append(list(map(int, input().split())))

    for m in mat:
        reversed(m)