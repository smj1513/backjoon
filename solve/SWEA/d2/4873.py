T = int(input())
for tc in range(T):
    string = input()
    stack = []
    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    print(f"#{tc+1}",len(stack))