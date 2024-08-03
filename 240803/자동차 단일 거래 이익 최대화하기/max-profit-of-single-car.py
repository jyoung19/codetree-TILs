n = int(input())

arr = list(map(int, input().split()))

new_arr = []

for i in range(len(arr)):
    for j in range(1, len(arr)-i):
        if arr[i] < arr[i+j]:
            new_arr.append(arr[i+j] - arr[i])

print(max(new_arr))