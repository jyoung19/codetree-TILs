n = int(input())
arr = [input() for _ in range(n)]

total_length = 0
cnt = 0

for string in arr:
    total_length += len(string)
    if string[0] == 'a':
        cnt += 1

print(total_length, cnt)