T = int(input())
for tc in range(T):
    P, Q, R, S, W = map(int, input().split())
    A_price = 0
    B_price = 0
    if W <= R:
        B_price = Q
    else:
        B_price = Q + (W-R)*S
    A_price = W*P
    print(f"#{tc+1}", min(A_price, B_price))