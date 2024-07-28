arr = list(input().split())

for i in range(len(arr)):
    if ((i+1) == 2) | ((i+1) == 5) | ((i+1) == 8):
        print(arr[i], end=" ")