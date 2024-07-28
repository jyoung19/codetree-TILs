arr = list(map(int, input().split()))
even_sum = 0
odd_sum = 0

for i in range(len(arr)):
    if (i+1) %2 == 0:
        even_sum += arr[i]
    else:
        odd_sum += arr[i]

print(abs(even_sum - odd_sum))