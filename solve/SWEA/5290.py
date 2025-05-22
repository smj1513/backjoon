T = int(input())
nums = [2, 3, 5, 7, 11]
for tc in range(T):
    N = int(input())
    abcde = [0] * 5
    for i in range(len(nums)):
        while N % nums[i] == 0:
            N //= nums[i]
            abcde[i] += 1
    print(f"#{tc+1}", *abcde)