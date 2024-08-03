N = int(input())
arr = list(map(int, input().split()))

max_idx = []

while len(arr) > 0:
    max_val = arr[0]
    max_pos = 0

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_pos = i

    max_idx.append(max_pos + 1)    
    arr = arr[:max_pos]

print(" ".join(map(str, max_idx)))