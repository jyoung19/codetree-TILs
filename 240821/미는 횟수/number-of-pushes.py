A = input()
B = input()
flag = False

for i in range(len(A)):
    A = A[-1] + A[:-1]
    if A == B:
        flag = True
        print(i+1)
        break

if (flag == False):
    print(-1)