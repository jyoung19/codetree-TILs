A, B = input().split()

AB = "".join(A + B)
BA = "".join(B + A)

print(int(AB) + int(BA))