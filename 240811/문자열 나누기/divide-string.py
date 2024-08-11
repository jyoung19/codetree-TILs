n = int(input())
arr = input()

# 공백 제거
num_arr = arr.replace(' ', '')

for i in range(len(num_arr)):
    print(num_arr[i], end='')
    
    # 5개씩 출력하면 그 다음 줄로
    if (i+1)%5 == 0:
        print()