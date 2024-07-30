count_arr = [0] * 10

arr = list(map(int, input().split()))

for num in arr:
    if num == 0:
        break
    ten_digits = num//10
    count_arr[ten_digits] += 1

for i in range(1, 10):
    cnt = count_arr[i]
    print(f"{i} - {cnt}")