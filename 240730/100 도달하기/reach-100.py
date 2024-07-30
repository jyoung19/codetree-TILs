n = int(input())
arr = [1, n]

i = 0

while (True):
    new_value = arr[i] + arr[i+1]
    arr.append(new_value)
    print(arr[i], end=" ")
    i += 1

    if arr[i] > 100:
        print(arr[i], end=" ")
        break