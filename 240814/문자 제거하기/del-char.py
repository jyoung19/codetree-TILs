def remove_character(string):
    while len(string) > 1:
        # 정수 입력 받기
        idx = int(input())
        
        # 주어진 정수가 문자열의 길이보다 크거나 같으면 마지막 문자를 제거
        if idx >= len(string):
            string = string[:-1]
        else:
            # 정수에 해당하는 위치의 문자를 제거
            string = string[:idx] + string[idx + 1:]
        
        # 제거 후 결과 출력
        print(string)

# 입력 받기
string = input().strip()

# 문자 제거 함수 호출
remove_character(string)