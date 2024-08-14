def process_requests(string, requests):
    for request in requests:
        if request == '1':
            # 가장 앞에 있는 문자를 뒤로 보냄
            string = string[1:] + string[0]
        elif request == '2':
            # 가장 뒤에 있는 문자를 앞으로 보냄
            string = string[-1] + string[:-1]
        elif request == '3':
            # 문자열을 좌우로 뒤집음
            string = string[::-1]
        # 요청을 처리한 후의 문자열 출력
        print(string)

# 입력 받기
initial_input = input().strip().split()
string = initial_input[0]
q = int(initial_input[1])

requests = [input().strip() for _ in range(q)]

# 함수 호출
process_requests(string, requests)