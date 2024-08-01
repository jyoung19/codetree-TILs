a, b = map(int, input().split())

# 나머지를 저장할 배열
res = []

# a가 1이하가 되기 전까지 나눗셈 반복
while (True):
    a = a // b
    res.append(a % b)
    if a <= 1:
        break

n = len(res)
count_arr = [0] * n

# 나머지들이 등장한 횟수를 배열로 저장
for num in res:
    count_arr[num] += 1

# 횟수를 제곱하여 그 합을 출력
sum = 0

for i in range(len(count_arr)):
    sum += count_arr[i] ** 2

print(sum)