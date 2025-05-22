T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sums = []
    if len(A) < len(B):
        for i in range(len(B) - len(A) + 1):
            sub = B[i:i+len(A)]
            sum = 0
            for j in range(len(A)):
                sum += A[j] * sub[j]
            sums.append(sum)
    elif len(A) > len(B):
        for i in range(len(A) - len(B) + 1):
            sub = A[i:i + len(B)]
            sum = 0
            for j in range(len(B)):
                sum += B[j] * sub[j]
            sums.append(sum)
    else:
        sum = 0
        for i in range(len(A)):
            sum += A[i] * B[i]
        sums.append(sum)
    print(f"#{tc+1}", max(sums))


