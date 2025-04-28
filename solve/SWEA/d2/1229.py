result = []
for _ in range(10):
    origin_len = int(input())
    origins = list(map(int, input().split()))
    c_count = int(input())
    inputs = input().split()
    sub_list = []
    for i in range(len(inputs)):
        if inputs[i] == 'I':
            y = int(inputs[i+2])
            sub_list.append(inputs[i:i+3+y])
        if inputs[i] == 'D':
            sub_list.append(inputs[i:i+3])
    for sub in sub_list:
        for j in sub:
            if j == 'I':
                c = sub.pop(0)
                x = int(sub.pop(0))
                y = sub.pop(0)
                for k in reversed(sub):
                    origins.insert(x, k)
            elif j == 'D':
                c = sub.pop(0)
                x = int(sub.pop(0))
                y = int(sub.pop(0))
                for k in range(y):
                    origins.pop(x)
    result.append(origins)
for i in range(len(result)):
    print(f"#{i+1}", *result[i][:10])
