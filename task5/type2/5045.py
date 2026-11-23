from string import printable as p


def convert(num, sys):
    res = ''
    while num:
        res += p[num % sys]
        num //= sys
    return res[::-1] if res else '0'


ans = []
for N in range(1, 10000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert(sum(map(int, R)) * 3, 3)
    R = int(R, 3)
    if (R % 2 != 0) and R > 208:
        ans.append(R)
print(min(ans))