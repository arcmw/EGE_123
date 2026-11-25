from itertools import product
ans = []
alph = sorted('ПОБЕДА')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] in 'О' and val.count('П') == 1 and val.count('О') and val.count('Б') and val.count('Е') and val.count('Д') and val.count('А') and pos % 2 == 0:
        ans.append([pos,val])
print(max(ans))