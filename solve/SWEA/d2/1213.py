result = []
for _ in range(10):
    _ = input()
    target = input()
    st = input()
    count = 0
    li = st.split(target)
    result.append(len(li)-1)
for i in range(10):
    print(f"#{i+1}", result[i])