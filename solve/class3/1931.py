import sys
read = sys.stdin.readline
N = int(read())
time_table = []
for i in range(N):
    time_table.append(tuple(map(int, read().strip().split())))
time_table.sort(key=lambda x:(x[1], x[0]))
#종료시간을 기준으로 정렬해서
#첫 회의가 끝나는 시간 <= 두 번째 회의 시작 시간
#위 조건이 일치하면 두 번째 회의 시작 시간을 회의 끝나는 시간 <= 세번째 회의 시작시간
end_time = 0
cnt = 0
for start, end in time_table:
    if end_time <= start:
       cnt += 1
       end_time = end
print(cnt)