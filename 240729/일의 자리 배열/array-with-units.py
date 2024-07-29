a, b = map(int, input().split())
arr = [a, b, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2, 10):
    arr[i] = (arr[i-2] + arr[i-1]) % 10

for i in range(len(arr)):
    print(arr[i], end=" ")