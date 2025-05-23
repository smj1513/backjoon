N = int(input())
nums = [str(i) for i in range(1, N+1)]
for n in nums:
    n = n.replace('3', '-').replace('6', '-').replace('9', '-')
    if n.count('-')>0:
        print('-'*n.count('-'), end=' ')
    else:
        print(n, end=' ')