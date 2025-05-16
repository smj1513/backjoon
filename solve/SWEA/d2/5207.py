def b_search(li, left, right, target, before_side):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if li[mid] == target:
            return mid
        elif li[mid] > target:
            if before_side == "left":
                return -1
            return b_search(li, left, mid - 1, target, "left")
        elif li[mid] < target:
            if before_side == "right":
                return -1
            return b_search(li, mid + 1, right, target, "right")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for b in B:
        result = b_search(A, 0, len(A)-1, b, "mid")
        if result != -1:
            cnt += 1
    print(f"#{tc+1}", cnt)