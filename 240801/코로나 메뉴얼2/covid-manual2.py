people = []
for _ in range(3):
    symptom, temperature = input().split()
    temperature = float(temperature)
    people.append((symptom, temperature))

A, B, C, D = 0, 0, 0, 0

for symptom, temperature in people:
    if symptom == 'Y' and temperature >= 37:
        A += 1
    elif symptom == 'N' and temperature >= 37:
        B += 1
    elif symptom == 'Y' and temperature < 37:
        C += 1
    else:
        D += 1

print(A, B, C, D, end=" ")

if A >= 2:
    print("E")