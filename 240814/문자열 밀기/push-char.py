def left_shift(string):
    # 첫 번째 문자를 잘라내고 나머지 부분과 결합
    shifted_string = string[1:] + string[0]
    
    # 결과 출력
    print(shifted_string)

# 입력 받기
string = input().strip()

# 함수 호출
left_shift(string)