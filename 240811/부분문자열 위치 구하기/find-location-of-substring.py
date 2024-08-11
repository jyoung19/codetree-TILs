str1 = input()
key = input()

n = len(key)
flag = False

for i in range(len(str1) - n):
    if str1[i:i+n] == key:
        flag = True
        print(i)

if flag == False:
    print(-1)