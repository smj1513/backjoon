result = []
for _ in range(10):
    _ = input()
    nums = list(map(int, input().split()))
    i = 1
    cycle_cnt = 0
    while nums[-1] > 0 :
        num = nums.pop(0)
        num -= i
        if num <= 0:
            num = 0
        nums.append(num)
        i += 1
        cycle_cnt += 1
        if cycle_cnt == 5:
            i = 1
            cycle_cnt = 0
    result.append(nums)

for i in range(10):
    print(f"#{i+1}", *result[i])