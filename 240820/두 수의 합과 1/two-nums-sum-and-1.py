a, b = map(int, input().split())
num = a + b

cnt = 0
for char in str(num):
    if char == '1':
        cnt += 1

print(cnt)