n = int(input())
num_arr = list(map(int, input().split()))

count = 0

for index, number in enumerate(num_arr):
    if number == 2:
        count += 1
    if count == 3:
        print(index + 1)
        break