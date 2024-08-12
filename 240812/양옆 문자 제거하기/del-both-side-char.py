str1 = input()
arr = list(str1)

arr.pop(1)
arr.pop(-2)

print(''.join(arr))