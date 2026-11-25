from itertools import product

ans = []
alph = sorted('АЛКМНЯ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] in 'К' and val[1] in 'М':
        ans.append([pos,val])
print(min(ans))
