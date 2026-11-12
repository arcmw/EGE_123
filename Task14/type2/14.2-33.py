from string import printable as p

for x in p[:26]:
    n = int(f'27{x}98876', 26) + int(f'26{x}51', 26) + int(f'15{x}47', 26) + int(f'62{x}5', 26)
    if n % 25 == 0:
        print(n // 25)