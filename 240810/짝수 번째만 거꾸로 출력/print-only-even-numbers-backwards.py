s = input()
e = ""

for i in range(len(s)):
    if i % 2 != 0:
        e += s[i]

print(e[::-1])