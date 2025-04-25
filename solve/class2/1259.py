num = 1
result = []
while num != 0:
    num = input()
    if num == '0': break
    is_palindrome = True
    for i in range(0, len(num)//2):
        if num[i] != num[len(num)-i-1]:
            is_palindrome = False
            break
    result.append("yes" if is_palindrome else "no")
    num = int(num)
for i in result:
    print(i)