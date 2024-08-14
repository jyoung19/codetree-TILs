def right_shift_repeated(string):
    L = len(string)
    
    # 처음 문자열 출력
    print(string)
    
    # 문자열을 한 글자씩 오른쪽으로 밀며 출력
    for _ in range(L - 1):
        # 마지막 문자를 앞으로 가져오고 나머지 문자열을 뒤로 이동
        string = string[-1] + string[:-1]
        print(string)

# 입력 받기
string = input().strip()

# 함수 호출
right_shift_repeated(string)