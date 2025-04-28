strs = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
result = []
t = int(input())
for _ in range(t):
    tc_n, tc_l = input().split()
    tc = input().split()
    result.append(sorted(tc, key=lambda x:strs[x]))

for i in range(len(result)):
    print(f"#{i+1}")
    for j in result[i]:
        print(j, end=" ")
    print()