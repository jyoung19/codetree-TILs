while True:
    s = input()
    if s == 'END':
        break
    else:
        arr = list(s)
        output = ''.join(arr[::-1])
        print(output)