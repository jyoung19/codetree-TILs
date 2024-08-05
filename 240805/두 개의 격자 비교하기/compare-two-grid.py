# 입력받기
n, m = map(int, input().split())

# 첫 번째 격자 입력
grid1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid1.append(row)

# 두 번째 격자 입력
grid2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid2.append(row)

# 결과를 저장할 격자 초기화
result = [[0] * m for _ in range(n)]

# 두 격자를 비교하여 결과를 생성
for i in range(n):
    for j in range(m):
        if grid1[i][j] == grid2[i][j]:
            result[i][j] = 0
        else:
            result[i][j] = 1

# 결과 격자 출력
for row in result:
    print(' '.join(map(str, row)))