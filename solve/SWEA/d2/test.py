import sys
from collections import Counter
read = sys.stdin.readline
N = int(read())

items = dict(Counter(map(int, read().split())).items())

M = int(read())
li2 = list(map(int, read().split()))
for i in li2:
    if i in items.keys():
        print(items[i], end=" ")
    else:
        print(0, end=" ")
