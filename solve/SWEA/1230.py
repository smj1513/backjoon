for tc in range(10):
    N = int(input())
    origins = list(map(int,input().split()))
    command_count = int(input())
    commands = list(input().split())
    for i in range(len(commands)):
        if commands[i] == 'I':
            x = int(commands[i+1])
            y = int(commands[i+2])
            s = commands[i+3:i+3+y]
            for s_n in reversed(s):
                origins.insert(x, s_n)
        elif commands[i] == 'D':
            x = int(commands[i+1])
            y = int(commands[i+2])
            for n in range(y):
                origins.pop(x+1)
        elif commands[i] == 'A':
            y = int(commands[i+1])
            s = commands[i+2:i+2+y]
            for s_n in s:
                origins.append(s_n)
    print(f"#{tc+1}", *origins[:10])