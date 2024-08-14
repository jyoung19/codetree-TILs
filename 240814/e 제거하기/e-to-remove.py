def remove_first_e(string):
    # 첫 번째 e의 인덱스 찾기
    index = string.find('e')
    
    # 첫 번째 e를 제거한 문자열 만들기
    new_string = string[:index] + string[index + 1:]
    
    # 결과 출력
    print(new_string)

# 입력 받기
string = input().strip()

# 함수 호출
remove_first_e(string)