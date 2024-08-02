import sys

N = int(input())

num_arr = list(map(int, input().split()))

min_val = sys.maxsize

for number in num_arr:
    if number < min_val:
        min_val = number

count = 0
    
for number in num_arr:
    if number == min_val:
        count += 1

print(min_val, count)