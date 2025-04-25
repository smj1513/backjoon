from datetime import date
N = int(input())
result = []
for _ in range(N):
    one_month, one_day, two_month, two_day = map(int, input().split())
    one_date = date(2025, one_month, one_day)
    two_date = date(2025, two_month, two_day)
    result.append((two_date - one_date).days + 1)

for i in range(len(result)):
    print(f'#{i+1}', result[i])