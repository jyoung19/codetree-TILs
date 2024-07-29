n = int(input())
i = 1
count = 0

while(True):
    value = n * i
    print(value, end=" ")
    if value % 5 == 0:
        count += 1
    if count == 2:
        break
    i += 1