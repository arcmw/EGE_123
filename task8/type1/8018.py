from itertools import product

ans = []
alph = sorted('АВОРТ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'ВОРОТА':
        ans.append(pos)
print(ans)