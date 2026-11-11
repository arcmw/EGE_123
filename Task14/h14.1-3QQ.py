from string import printable as pr
sys = int()

def convert(num, sys):  # 58
    res = ''  #
    while num:  # 58
        res += pr[num % sys]
        num //= sys  # 29
    return res[::-1] if res else '0'

if convert(41, sys)[-1:] == 2 and convert(131, sys)[-1] == 1:

    print(sys)
