arr = ["apple", "banana", "grape", "blueberry", "orange"]
given_letter = input()
cnt = 0

for i in range(len(arr)):
    if (given_letter == arr[i][2]) | (given_letter == arr[i][3]):
        print(arr[i])
        cnt += 1

print(cnt)