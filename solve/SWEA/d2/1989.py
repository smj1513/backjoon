T = int(input())
for tc in range(T):
    string = input()
    isPalindrome = True
    for i in range(len(string)):
        if string[i] != string[-(i+1)]:
            isPalindrome = False
            break
    print(f"#{tc+1}", "1" if isPalindrome else "0")