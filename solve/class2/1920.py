import sys
read = sys.stdin.readline
N, M = map(int, read().split())
pedia = dict()
reversed_dict = dict()
for i in range(1, N+1):
    monster = read().strip()
    pedia.update({str(i):monster})
    reversed_dict.update({monster:str(i)})

for _ in range(M):
    command = read().strip()
    print(pedia[command] if command in pedia else reversed_dict[command])