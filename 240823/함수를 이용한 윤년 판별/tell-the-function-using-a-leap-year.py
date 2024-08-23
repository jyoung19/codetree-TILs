def func(n):
    if n % 4 == 0:
        return "true"
    elif (n % 100 == 0) and (n % 400 != 0):
        return "false"
    else:
        return "false"
    
y = int(input())
print(func(y))