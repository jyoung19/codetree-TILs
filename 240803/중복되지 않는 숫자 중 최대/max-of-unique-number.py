N = int(input())
arr = list(map(int, input().split()))

dict = {}
for num in arr:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

unique_num = []

for key, value in dict.items():
 if value == 1:
    unique_num.append(key)

if len(unique_num) == 0:
    print(-1)
else:
    max_val = unique_num[0]
    for num in unique_num:
        if max_val < num:
            max_val = num
    print(max_val)