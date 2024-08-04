n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

idxs = list(filter(lambda x: A[x] == B[0], range(len(A))))
flag = False

if B[0] in A:
    for idx in idxs:
        for i in range(len(B)):
            if B[i] == A[idx + i]:
                flag = True
            else:
                flag = False
                break

if flag == True:
    print("Yes")
else:
    print("No")