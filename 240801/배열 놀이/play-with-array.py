n, q = map(int, input().split())

# n개의 원소 입력받기
arr1 = list(map(int, input().split()))

query_arr = []

# q개의 질의 입력받기
for _ in range(q):
    arr2 = list(map(int, input().split()))
    query_arr.append(arr2)

for i in range(len(query_arr)):
    # "1 a"
    if query_arr[i][0] == 1:
        print(arr1[query_arr[i][1] - 1])  # a번째 원소 출력
    # "2 b"
    elif query_arr[i][0] == 2:
        if query_arr[i][1] in arr1:
            print(arr1.index(query_arr[i][1]) + 1)  # 몇 번째 원소인지 출력
        else:
            print(0)
    # "3 s e"
    elif query_arr[i][0] == 3:
        s = query_arr[i][1]
        e = query_arr[i][2]
        for i in range(s, e+1):  # s번째 원소부터 e번째 원소까지 출력
            print(arr1[i-1], end=" ")