from string import printable as p

X = int()
N = 3 * 7 ** (X + 1) + 13 * 7 ** (X + 2) + 31 * 7 ** (3 * X) + 1 * 7 ** (2 * X)
R = ''
while N:
    R = R + p[N % 7]
    N = N // 7

if sum(map(int, R)) == 18:
    print (X)






