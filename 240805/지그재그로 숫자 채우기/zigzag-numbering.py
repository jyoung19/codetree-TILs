# 입력 받기
n, m = map(int, input().split())

# 결과를 저장할 2차원 배열 초기화
matrix = [[0] * m for _ in range(n)]

# 지그재그로 배열 채우기
num = 0
for col in range(m):
    if col % 2 == 0:
        # 짝수 열: 위에서 아래로 채우기
        for row in range(n):
            matrix[row][col] = num
            num += 1
    else:
        # 홀수 열: 아래에서 위로 채우기
        for row in range(n-1, -1, -1):
            matrix[row][col] = num
            num += 1

# 결과 출력
for row in matrix:
    print(' '.join(map(str, row)))