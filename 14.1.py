ans = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 8 == 0:
        R = str(R) + str(R)[-2:]
    else:
        R = R + bin((N % 8) * 2)[2:]
    R = int(R,2)
    if R > 3000:
        print(N)
