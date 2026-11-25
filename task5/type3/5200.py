ans = []
for N in range(1, 10000):
    R = oct(N)[2:]
    if R.count('2') + R.count('4') + R.count('6') % 2 != 0:
        R += '46'
    else:
        R = oct((N % 8)*5)[2:] + R
    R = int(R, 8)
    if R == N:
        ans.append(N)
print(min(ans))
