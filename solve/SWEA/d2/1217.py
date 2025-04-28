def pow(n, m):
    if m == 1:
        return n
    return n * pow(n, m-1)

result = []
for _ in range(10):
    t = int(input())
    n, m = map(int, input().split())
    result.append(pow(n, m))

for i in range(len(result)):
    print(f"#{i+1}", result[i])
