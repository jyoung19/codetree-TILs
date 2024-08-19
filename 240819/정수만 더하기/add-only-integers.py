A = input()  # 입력 문자열 받기
total = 0

for char in A:
    if char.isdigit():  # 문자가 숫자인지 확인
        total += int(char)

print(total)  # 최종 결과 출력