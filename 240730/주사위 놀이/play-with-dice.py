count_arr = [0] * 6

arr = list(map(int, input().split()))

for element in arr:
    count_arr[element - 1] += 1


for i in range(1, 7):
    cnt = count_arr[i-1]
    print(f"{i} - {cnt}")