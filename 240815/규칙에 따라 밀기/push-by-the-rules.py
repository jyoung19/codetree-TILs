# 입력받기
A = input()
commands = input()

# 명령을 순차적으로 처리
for command in commands:
    if command == 'L':
        # 왼쪽으로 한 칸 밀기: 첫 번째 문자를 맨 뒤로 보낸다.
        A = A[1:] + A[0]
    elif command == 'R':
        # 오른쪽으로 한 칸 밀기: 마지막 문자를 맨 앞으로 보낸다.
        A = A[-1] + A[:-1]

# 최종 결과 출력
print(A)