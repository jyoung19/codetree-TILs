n, m = map(int, input().split())

arr_2d = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    r, c = map(int, input().split())
    arr_2d[r-1][c-1] = r*c

for row in arr_2d:
    for elem in row:
        print(elem, end=' ')
    print()