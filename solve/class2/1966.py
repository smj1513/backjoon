T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    result = 1
    while queue:
        if queue[0] < max(queue):
            queue.append(queue.pop(0))
        else:
            if M == 0:
                break
            queue.pop(0)
            result += 1
        M = M - 1 if M > 0 else len(queue) - 1
    print(result)