count_arr = [0] * 11

arr = list(map(int, input().split()))

for num in arr:
    if num == 0:
        break
    ten_digits = num//10
    count_arr[ten_digits] += 1

for i in range(10, 0, -1):
    cnt = count_arr[i]
    points = i * 10
    print(f"{points} - {cnt}")