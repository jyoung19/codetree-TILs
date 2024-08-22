def func(n, m):
    i = max(n, m)
    while True:
        if (i % n == 0) & (i % m == 0):
            break
        i += 1
    print(i)

n, m = tuple(map(int, input().split()))
func(n, m)