def count_special_numbers(a, b):
    def is_special(num):
        # 숫자에 3, 6, 9가 포함되어 있거나 3의 배수인지 확인
        if '3' in str(num) or '6' in str(num) or '9' in str(num) or num % 3 == 0:
            return True
        return False

    count = 0
    for num in range(a, b + 1):
        if is_special(num):
            count += 1

    return count

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
print(count_special_numbers(a, b))