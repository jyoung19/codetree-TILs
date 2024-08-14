def remove_substring(A, B):
    # 문자열 B가 A에 더 이상 존재하지 않을 때까지 반복
    while B in A:
        # B의 첫 번째 등장 위치 찾기
        index = A.find(B)
        
        # B를 제거한 새로운 문자열 생성
        A = A[:index] + A[index + len(B):]
    
    # 최종 문자열 출력
    print(A)

# 입력 받기
A = input().strip()
B = input().strip()

# 함수 호출
remove_substring(A, B)