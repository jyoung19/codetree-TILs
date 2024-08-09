n = int(input())
arr = []

for i in range(n):
    word = input()
    arr.append(word)

given_char = input()
cnt = 0

arr2 = []

for word in arr:
    if word.startswith(given_char):
        cnt += 1
        arr2.append(word)

total_length = 0

for word in arr2:
    total_length += len(word)

print(cnt, f'{total_length/len(arr2):.2f}')