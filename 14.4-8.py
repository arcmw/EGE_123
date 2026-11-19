from math import log2, ceil
ans=[]
for L in range(1, 10000):
    N = 10 + 52 + 972
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 2048 * I > 172*1024:
      ans.append(L)
print(min(ans))
