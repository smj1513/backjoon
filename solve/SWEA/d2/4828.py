N = int(input())
result = []
for n in range(N):
    m = int(input())
    nums = list(map(int, input().split()))
    result.append( max(nums) - min(nums))

for i in range(len(result)):
    print(f"#{i+1}", result[i])