str1 = input()
cnt1, cnt2 = 0, 0

for i in range(len(str1) - 1):
    if str1[i:i+2] == 'ee':
        cnt1 += 1
    if str1[i:i+2] == 'eb':
        cnt2 += 1

print(cnt1, cnt2)