s = input()
result = ""

current_char = s[0]
count = 1

# 문자열을 순차적으로 순회
for i in range(1, len(s)):
    if s[i] == current_char:
        count += 1
    else:
        # 현재 문자와 그 개수를 결과에 추가
        result += current_char + str(count)
        # 다음 문자로 넘어가면서 초기화
        current_char = s[i]
        count = 1

# 마지막 문자와 그 개수 추가
result += current_char + str(count)

print(len(result))
print(result)