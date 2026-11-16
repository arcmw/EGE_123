from math import log2,ceil

for N in range(1,10000):
    L = 2783
    i = ceil(log2(N))
    I = ceil(L * i/8)
    if 3845627 * I >= 11 * 2**30:
        print(N)
        break