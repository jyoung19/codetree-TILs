def func(n):
    if (n % 4 == 0) and (n % 100 == 0) and (n % 400 != 0):
        return "false"
    elif (n % 100 != 0) or (n % 400 == 0):
        return "true"
    else:
        return "false"
    
y = int(input())
print(func(y))