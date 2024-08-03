N = int(input())
arr = list(map(int, input().split()))

# 선택 정렬을 이용한 내림차순 정렬
for i in range(N):
    max_idx = i
    for j in range(i + 1, N):
        if arr[j] > arr[max_idx]:
            max_idx = j
    arr[i], arr[max_idx] = arr[max_idx], arr[i]

# 내림차순으로 정렬된 배열에서 첫 번째와 두 번째 원소 출력
print(arr[0], arr[1])