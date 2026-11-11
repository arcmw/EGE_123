n = 4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49
res = set()
while n:
    res.add(n % 16)
    n //= 16
print(len(res))