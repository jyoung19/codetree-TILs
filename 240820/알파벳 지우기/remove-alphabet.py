str1 = input()
str2 = input()

def func(s):
    num_str = ''
    for char in s:
        if char.isdigit():
            num_str += char
    return int(num_str)

num1 = func(str1)
num2 = func(str2)

print(num1 + num2)