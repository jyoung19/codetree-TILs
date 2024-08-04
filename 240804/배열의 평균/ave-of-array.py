arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

sum_rows = []
sum_cols = []

for i in range(2):
    sum_row = 0
    for j in range(4):
        sum_row += arr_2d[i][j]
    sum_rows.append(sum_row)

for j in range(4):
    sum_col = 0
    for i in range(2):
        sum_col += arr_2d[i][j]
    sum_cols.append(sum_col)

print(' '.join(str(sums/4) for sums in sum_rows))
print(' '.join(str(sums/2) for sums in sum_cols))
print(round(sum(sum_rows)/8, 1))