from string import printable as p

for x in p[:20]:
    n = int(f'627{x}j8',20) + int(f'h45i{x}5hij',20) + int(f'4idb49j{x}7',20)
    if n % 19 == 0:
        print(n//19)