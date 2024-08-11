A = input()
B = input()

n = len(B)
cnt = 0

for i in range(len(A) - n):
    if A[i:i+n] == B:
        cnt += 1

print(cnt)