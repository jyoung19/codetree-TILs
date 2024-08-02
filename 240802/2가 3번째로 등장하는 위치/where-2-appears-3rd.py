n = int(input())
num_arr = list(map(int, input().split()))

count = 0

for i in range(len(num_arr)):
    if num_arr[i] == 2:
        count += 1
    if count == 3:
        print(i + 1)
        break