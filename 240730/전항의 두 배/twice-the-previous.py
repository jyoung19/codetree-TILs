arr = list(map(int, input().split()))

for i in range(2, 11):
    new_value = arr[i-1] + 2 * arr[i-2]
    arr.append(new_value)

for i in range(10):
    print(arr[i], end=" ")