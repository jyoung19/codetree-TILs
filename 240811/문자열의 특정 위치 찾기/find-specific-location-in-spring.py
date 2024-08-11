str1, char = input().split()

if str1.find(char) == -1:
    print('No')
else:
    print(str1.find(char))