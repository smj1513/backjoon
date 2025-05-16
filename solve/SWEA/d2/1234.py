result = []
for _ in range(10):
    N, password = input().split()
    ans = []
    for p in password:
        if not ans or ans[-1] != p:
            ans.append(p)
        else:
            ans.pop()

    result.append(''.join(ans))

for r in range(len(result)):
    print(f"#{r+1}",result[r])