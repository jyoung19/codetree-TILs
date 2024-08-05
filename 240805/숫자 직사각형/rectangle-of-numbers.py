# n과 m의 값을 입력받습니다
n, m = map(int, input().split())

# 2차원 배열을 초기화합니다
rectangle = [[0] * m for _ in range(n)]

# 배열에 순차적인 숫자를 채워넣습니다
num = 1
for i in range(n):
    for j in range(m):
        rectangle[i][j] = num
        num += 1

# 배열을 출력합니다
for row in rectangle:
    print(' '.join(map(str, row)))