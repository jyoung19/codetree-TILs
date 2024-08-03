n = int(input())
arr = list(map(int, input().split()))

min_diff = arr[1] - arr[0]

for i in range(1, n-1):
    diff = arr[i+1] - arr[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)