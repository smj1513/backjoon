result = []
for _ in range(10):
    dump = int(input())
    blocks = list(map(int, input().split()))
    for i in range(dump):
        max_idx = blocks.index(max(blocks))
        min_idx = blocks.index(min(blocks))
        blocks[max_idx] -= 1
        blocks[min_idx] += 1

        if blocks[max_idx] - blocks[min_idx] <= 1:
            break
    result.append(max(blocks)-min(blocks))
for i in range(10):
    print(f"#{i+1}", result[i])