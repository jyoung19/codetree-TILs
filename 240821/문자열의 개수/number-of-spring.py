arr = []

while True:
    s = input()
    if s == '0':
        break
    else:
        arr.append(s)

print(len(arr))  # 입력받은 모든 문자열의 개수 출력
for i in range(len(arr)):
    if (i+1) % 2 != 0:  # 홀수 번째로 주어진 문자열 출력
        print(arr[i])