def func(N):
    total = 0
    for i in range(1, N+1):
        total += i
    return (total // 10)

N = int(input())
print(func(N))