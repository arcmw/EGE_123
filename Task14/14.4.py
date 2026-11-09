num = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
res = set()
while num:
    res.add(num % 15)
    num //= 15
print(len(res))
