from math import ceil, log2

for t in range(1,10000):
    d = 1024*960
    N = 8192
    i = ceil(log2(N))
    v = ceil((d * i * 160) / 14680064)
    print(v)
    break