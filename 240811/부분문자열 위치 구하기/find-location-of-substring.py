str1 = input()
key = input()

n = len(key)
flag = False

for i in range(len(str1)):
    if str1[i:i+n] == key:
        flag = True
        print(i)
        break

if flag == False:
    print(-1)