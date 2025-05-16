import sys
read = sys.stdin.readline
s = set()
M = int(read())
for _ in range(M):
    temp = read().strip()
    command = ""
    num = 0
    if temp.startswith("all") or temp.startswith("empty"):
        command = temp
    else:
        command, num = temp.split()
        num = int(num)
    if command == "add":
        s.add(num)
    elif command == "remove":
        s.discard(num)
    elif command == "check":
        print(1 if num in s else 0)
    elif command == "empty":
        s.clear()
    elif command == "all":
        s = set([i for i in range(1, 21)])
    elif command == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)