def extract_integer_from_string(s):
    num_str = ''
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            break
    return int(num_str)

# 입력 받기
input_str = input().strip()

# 공백으로 문자열 분리
str1, str2 = input_str.split()

# 각 문자열에서 정수 부분 추출
num1 = extract_integer_from_string(str1)
num2 = extract_integer_from_string(str2)

# 두 정수의 합 계산
result = num1 + num2

# 결과 출력
print(result)