def add(a, c):
    return a + c

def subtract(a, c):
    return a - c

def multiply(a, c):
    return a * c

def divide(a, c):
    return a // c  # 정수 부분만 출력

def calculate(a, o, c):
    if o == '+':
        return f"{a} + {c} = {add(a, c)}"
    elif o == '-':
        return f"{a} - {c} = {subtract(a, c)}"
    elif o == '*':
        return f"{a} * {c} = {multiply(a, c)}"
    elif o == '/':
        return f"{a} / {c} = {divide(a, c)}"
    else:
        return False

# 입력 받기
a, o, c = input().split()
a = int(a)
c = int(c)

# 결과 출력
result = calculate(a, o, c)
print(result)