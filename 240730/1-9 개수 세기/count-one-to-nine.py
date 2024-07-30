count_arr = [0] * 9

n = int(input())

# 개수 세기
arr = list(map(int, input().split()))
for elem in arr:
    count_arr[elem - 1] += 1

# 개수 출력
for i in range(len(count_arr)):
    print(count_arr[i])