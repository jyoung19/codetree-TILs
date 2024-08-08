str1 = input()
str2 = input()
str3 = input()

shortest = min(len(str1), len(str2), len(str3))
longest = max(len(str1), len(str2), len(str3))

print(longest - shortest)