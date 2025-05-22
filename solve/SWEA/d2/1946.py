T = int(input())
for tc in range(T):
    N = int(input())
    alphas = [tuple(input().split()) for _ in range(N)]
    print(f"#{tc+1}", end='')
    i = 0
    for alpha, num in alphas:
        for _ in range(int(num)):
            if i % 10 == 0:
                print()
            i+=1
            print(alpha, end='')
    print()