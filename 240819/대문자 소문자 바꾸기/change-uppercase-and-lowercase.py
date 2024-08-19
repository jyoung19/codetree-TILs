str1 = input()  # 입력 문자열 받기
result = ""  # 결과 문자열 초기화

for char in str1:
    if 'A' <= char and char <= 'Z':
        result += char.lower()  # 대문자인 경우 소문자로 변환하여 추가
    elif 'a' <= char and char <= 'z': 
        result += char.upper()  # 소문자인 경우 대문자로 변환하여 추가

print(result)  # 최종 결과 출력