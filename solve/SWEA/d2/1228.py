result = []
for _ in range(10):
    origin_len = int(input())
    origins = list(map(int, input().split()))
    c_count = int(input())
    inputs = input().split("I ")
    inputs.pop(0)
    for i in inputs:
        part = i.split()
        x = int(part[0])
        y = int(part[1])
        z = list(map(int, part[2:]))
        for j in reversed(z):
            origins.insert(x, j)
    result.append(origins[:10])

for i in range(len(result)):
    print(f"#{i+1}", *result[i])
