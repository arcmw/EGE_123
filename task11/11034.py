from math import log2, ceil

for N in range(1, 10000):
    i = ceil(log2(N))
    I = ceil(248 * i / 8)
    if I * 75600 > 16 * 1024 ** 2:
        print(N)
        break
