from string import printable as p
from itertools import product

ans = 0
for val in product(p[:16], repeat=3):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) == 3:
        for i in p[:16:2]:
            val = val.replace(i, '*')
        for i in p[1:16:2]:
            val = val.replace(i, '!')
        if '**' not in val and '!!' not in val:
            ans += 1
print(ans)

