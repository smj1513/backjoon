result = []
for _ in range(10):
    T = int(input())
    view_apt = 0
    apt = list(map(int, input().split()))
    for i in range(2, len(apt)-2):
        left_view_one = apt[i] - apt[i-1]
        left_view_two = apt[i] - apt[i-2]
        right_view_one = apt[i] - apt[i+1]
        right_view_two = apt[i] - apt[i+2]
        if left_view_two > 0 and left_view_one > 0 and right_view_one > 0 and right_view_two > 0:
            view_apt += min(left_view_one, left_view_two, right_view_two, right_view_one)
    result.append(view_apt)
for i in range(10):
    print(f"#{i+1}", result[i])