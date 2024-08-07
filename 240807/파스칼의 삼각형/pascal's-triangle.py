n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 1. 첫 번째 열과 각 행의 마지막 열에 전부 숫자 1을 채움
for j in range(n):
    arr_2d[j][0] = 1
    arr_2d[j][j] = 1

# 2. 나머지 칸에 전부 숫자를 채웁니다.
for i in range(1, n):
    for j in range(n):
        arr_2d[i][j] = arr_2d[i - 1][j - 1] + arr_2d[i - 1][j]

# 출력
for row in arr_2d:
    for elem in row:
        if elem == 0:
            pass
        else:
            print(elem, end=" ")
    print()