from math import ceil, log2


for B in range (1,10000):
    L = 110
    N = 10 + 1020
    i = ceil(log2(N))
    I = ceil((L * i) / 8)
    B = ceil((I * 32768) / 1024)
    print (B)
    break
