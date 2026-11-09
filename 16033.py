ans = []
for N in range(1, 10000):
    R = f"{2:b}"
    if N % 2 == 0:
        R += '01'
    elif N % 2 == 1:
        R += '10'
    R = int(R, 2)
    if R > 102:
        ans.append(N)
        print(min(ans))