N = int(input())
for tc in range(1, N+1):
    str1 = set(input())
    str2 = input()
    dict = {}
    #딕셔너리 배열 생성
    for c in str1:
        dict[c] = 0

    for c in str2:
        if c in str1:
            dict[c] += 1

    max_num = 0
    for v in dict.values():
        if v > max_num:
            max_num = v
    print(f"#{tc}", max_num)