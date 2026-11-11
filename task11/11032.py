from math import log2, ceil

for L in range(1, 10000):
    N = 963 + 52 + 10
    i = ceil(log2(N))
    I = ceil((L * i) / 8)
    if 2000 * I <= 693 * 1024:
        print(L)
