n = int(input())

total = 0
for _ in range(n):
    total += int(input())

str1 = str(total)
print(str1[1:] + str1[0])