from string import printable as p


def convert(num,sys):
    res = ''
    while num:
        res += p[num % sys]
        num //= sys
    return res[::-1] if res else '0'


ans=[]
for x in range(1,3001):
    num = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    sys = 11
    res = convert(num,sys)
    if res.count('0') == 60:
        ans.append(x)


print(max(ans))
