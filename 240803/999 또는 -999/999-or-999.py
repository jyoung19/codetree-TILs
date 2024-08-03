arr = list(map(int, input().split()))

for i in range(len(arr)):
    if (arr[i] == 999) | (arr[i] == -999):
        new_arr = arr[:i]
        break

min = new_arr[0]
max = new_arr[0]

for j in range(len(new_arr)):
    if new_arr[j] < min:
        min = new_arr[j]
    if new_arr[j] > max:
        max = new_arr[j]    
    
print(max, min)