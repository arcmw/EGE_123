num = 5 ** 2022 - 2 * 5 ** 1010 + 25 ** 850 + 2500
cnt = 0
while num:
    if num % 5 == 4:
        cnt += 1
    num //= 5
print(cnt)
