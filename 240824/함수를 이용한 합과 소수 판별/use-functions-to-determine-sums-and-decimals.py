def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits_is_even(n):
    return sum(int(digit) for digit in str(n)) % 2 == 0

def count_special_primes(a, b):
    count = 0
    for i in range(a, b + 1):
        if is_prime(i) and sum_of_digits_is_even(i):
            count += 1
    return count

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
result = count_special_primes(a, b)
print(result)