T = int(input())
def in_order(tree, N, i):
    global cnt
    if i > N:
        return
    else:
        in_order(tree, N, i * 2)
        tree[i] = cnt
        cnt += 1
        in_order(tree, N, i * 2 + 1)

for tc in range(T):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    in_order(tree, N, 1)
    print(f"#{tc+1}",tree[1], tree[N//2])