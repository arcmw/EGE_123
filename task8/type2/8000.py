from itertools import product

ans = 0

for val in product('школа', repeat=3):
    val = ''.join(val)
    if val.count('к') == 1:
        ans += 1
print(ans)
