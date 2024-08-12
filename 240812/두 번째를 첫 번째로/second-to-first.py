str1 = input()
arr = list(str1)

for i in range(2, len(arr)):
    if arr[i] == arr[1]:
        arr[i] = arr[0]
    
arr[1] = arr[0]

print(''.join(arr))