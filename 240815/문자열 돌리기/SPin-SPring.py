# 입력받은 문자열
s = input()

# 문자열의 길이
L = len(s)

# L회 반복하여 각 회마다 문자열을 회전시키고 출력
for i in range(L):
    rotated_string = s[-i:] + s[:-i]  # 오른쪽으로 i만큼 회전
    print(rotated_string)

# 마지막에 원래 문자열을 다시 출력
print(s)