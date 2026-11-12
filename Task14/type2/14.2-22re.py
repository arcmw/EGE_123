from string import printable as p

ans = []
for x in p[10: 14]:
    for y in p[9:int(x, 36)]:
        num1 = int(f'7{x}37{y}', 14)
        num2 = int(f'9{y}63', int(x, 36))
        num3 = int(f'15148', int(y, 36))
        num = num1 + num2 + num3
        ans.append([num, num // (int(x, 36) + int(y, 36))])
print(max(ans))
