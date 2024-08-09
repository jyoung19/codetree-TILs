arr = []

for i in range(10):
    word = input()
    arr.append(word)

given_char = input()
cnt = 0

for word in arr:
    if word.endswith(given_char):
        cnt += 1
        print(word)

if cnt == 0:
    print('None')