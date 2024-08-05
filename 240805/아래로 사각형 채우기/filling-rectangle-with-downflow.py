# 입력 받기
n = int(input())

# 결과를 저장할 2차원 배열 초기화
result = [[0] * n for _ in range(n)]

# 배열 채우기
for i in range(n):
    for j in range(n):
        result[i][j] = i + 1 + j * n

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))