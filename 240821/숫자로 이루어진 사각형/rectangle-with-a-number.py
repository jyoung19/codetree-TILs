N = int(input())

def print_rect(N):
    num = 1
    for i in range(N):
        for j in range(N):
            print(num, end=' ')
            num += 1
            if num == 10:
                num = 1
        print()

print_rect(N)