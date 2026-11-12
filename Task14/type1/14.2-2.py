n = 729 ** 8 - 3 ** 18 + 85
cnt = 0
while n:
    if n % 9 == 0: cnt += 1
    n //= 9
    print(cnt)
