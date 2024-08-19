str1 = input()  # 입력 문자열 받기
result = ""  # 결과 문자열 초기화

for char in str1:
    if char.isalpha():  # 문자가 알파벳인지 확인
        result += char.upper()  # 알파벳인 경우 대문자로 변환하여 추가

print(result)  # 최종 결과 출력