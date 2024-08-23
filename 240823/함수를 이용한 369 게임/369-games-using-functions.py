def func(a, b):
    cnt = 0
    for i in range(a, b+1):
         # 한 자리 수인 경우
        if i < 10: 
            if (i == 3) or (i == 6) or (i == 9):
                cnt += 1
        # 두 자리 수인 경우
        else:
            digit1 = i // 10  # 십의 자리 수
            digit2 = i % 10  # 일의 자리 수
            if (digit1 == 3) or (digit1 == 6) or (digit1 == 9):
                cnt += 1
            elif (digit2 == 3) or (digit2 == 6) or (digit2 == 9):
                cnt += 1
            elif i % 3 == 0:
                cnt += 1
    return cnt

a, b = map(int, input().split())
print(func(a, b))