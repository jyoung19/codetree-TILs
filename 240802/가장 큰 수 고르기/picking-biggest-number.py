num_arr = list(map(int, input().split()))

max_num = num_arr[0]

for number in num_arr:
    if number > max_num:
        max_num = number
    
print(max_num)