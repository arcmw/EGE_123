from itertools import product

ans = []
alph = sorted('ЯНВАРЬ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'Я' and val.count('Ь') <= 1:
        ans.append([pos, val])
print(ans)
