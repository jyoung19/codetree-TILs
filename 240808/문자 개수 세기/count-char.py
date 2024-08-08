given_input = input()
given_char = input()
cnt = 0

for char in given_input:
    if char == given_char:
        cnt += 1

print(cnt)