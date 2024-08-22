def func(n, m):
    for i in range(max(n, m), 0, -1):
        if (n % i == 0) & (m % i == 0):
            break
    print(i)

n, m = map(int, input().split())
func(n, m)