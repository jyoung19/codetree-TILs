arr = list(map(int, input().split()))
even_sum = 0
tsum = 0
count = 0

for i in range(10):
    if (i+1) %2 == 0:
        even_sum += arr[i]
    if (i+1) % 3 == 0:
        tsum += arr[i]
        count += 1

print(even_sum, tsum/count)