N = int(input())

arr = list(map(int, input().split()))

# 첫 번째로 가장 큰 수
max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

arr.remove(max_val)

# 두 번째로 가장 큰 수
max_val2 = arr[0]

for num in arr:
    if num > max_val2:
        max_val2 = num

print(max_val, max_val2)