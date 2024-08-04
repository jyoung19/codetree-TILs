n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

flag = False

if n2 <= n1:  # 수열 B가 수열 A보다 길 경우를 미리 체크
    idxs = [i for i in range(n1 - n2 + 1) if A[i] == B[0]]  # A의 가능한 시작 인덱스 찾기

    for idx in idxs:
        match = True
        for i in range(n2):
            if A[idx + i] != B[i]:
                match = False
                break
        if match:
            flag = True
            break  # 한 번이라도 일치하면 더 이상 확인할 필요 없음

if flag == True:
    print("Yes")
else:
    print("No")