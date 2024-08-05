def fill_diagonals(n, m):
    # 결과를 저장할 2차원 배열 초기화
    matrix = [[0] * m for _ in range(n)]
    
    num = 1  # 숫자를 1부터 시작
    
    # 대각선 채우기
    for s in range(n + m - 1):
        if s < m:
            # 시작점은 첫 번째 행의 각 열
            row = 0
            col = s
        else:
            # 시작점은 마지막 열의 각 행
            row = s - m + 1
            col = m - 1
        
        while row < n and col >= 0:
            matrix[row][col] = num
            num += 1
            row += 1
            col -= 1
    
    # 결과 출력
    for row in matrix:
        print(' '.join(map(str, row)))

# 입력 받기
n, m = map(int, input().split())
fill_diagonals(n, m)