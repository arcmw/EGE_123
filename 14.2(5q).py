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
    if sum(map(int, R)) % 3 == 0:
        R += '212'
    else:
        R += convert(2 * sum(map(int, R)), 3)

    R = int(R,3)
    if R > 490:
        ans.append(R)

print(min(ans))
