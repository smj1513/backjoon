T = int(input())
def get_count(tree, n ,visited):
    global cnt
    visited[n] = True

    if not tree[n]:
        return 0
    else:
        for i in tree[n]:
            if not visited[i]:
                cnt += 1
                get_count(tree, i, visited)

for tc in range(T):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+2)]
    visited = [False] * (E+2)
    nodes = list(map(int, input().split()))
    cnt = 0

    for i in range(0, len(nodes), 2):
        parents = tree[nodes[i]]
        parents.append(nodes[i+1])
    get_count(tree, N, visited)
    print(f"#{tc+1}", cnt+1)# 자기자신 +1


