def b_search(li: list, start: int, end: int, target: int):
    if start >= end:
        return False
    else:
        mid = (start + end) // 2
        if target == li[mid]:
            return True
        elif target > li[mid]:
            return b_search(li, mid + 1, end, target)
        else:
            return b_search(li, start, mid, target)


N = int(input())
li1 = sorted(list(map(int, input().split())))

M = int(input())
li2 = list(map(int, input().split()))

for i in li2:
    if b_search(li1, 0, len(li1), i):
        print(1)
    else:
        print(0)