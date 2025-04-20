alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
st = input()
count = 0
i = 0
while i < len(st):
    if alpha.__contains__(st[i:i+3]):
        i += 3
    elif alpha.__contains__(st[i:i+2]):
        i += 2
    else:
        i += 1
    count += 1

print(count)


# other version
# alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# st = input()
# for i in alpha:
#     st = st.replace(i, "x")
# print(len(st))