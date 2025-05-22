import sys
read = sys.stdin.readline
N, M = map(int, read().split())
sites = dict()
for _ in range(N):
    site, password = read().strip().split()
    sites.update({site:password})

for _ in range(M):
    site = read().strip()
    print(sites.get(site))