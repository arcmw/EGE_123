N = int()
for N in range(1, 10000):
    if N < 40 and bin(N)[-4:] == '1011':
        print(N)
