arr = list(map(int, input().split()))

over = []
under = []

for num in arr:
    if num < 500:
        under.append(num)
    elif num > 500:
        over.append(num)

max_val = under[0]
min_val = over[0]

for num in under:
    if num > max_val:
        max_val = num
for num in over:
    if num < min_val:
        min_val = num

print(max_val, min_val)