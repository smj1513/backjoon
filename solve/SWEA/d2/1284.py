from collections import Counter
T = int(input())

result = []

for _ in range(T):
    _ = input()
    inp = list(map(int, input().split())) #[41, 23 ...]
    result.append(Counter(inp).most_common())
for i in range(T):
    print(f"#{i+1}", result[i][0][0])