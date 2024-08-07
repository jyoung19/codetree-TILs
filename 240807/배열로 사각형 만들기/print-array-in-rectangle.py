n = 5
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 1. 첫 번째 행과 첫 번째 열은 모두 1로 초기화
for j in range(n):
    arr_2d[0][j] = 1
    arr_2d[j][0] = 1

# 2. 나머지 칸들은 바로 위의 값과 바로 왼쪽의 값을 더함
for i in range(1, n):
    for j in range(n):
        arr_2d[i][j] = arr_2d[i - 1][j] + arr_2d[i][j - 1]

# 출력
for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()