n=16**820-2**761+14
cnt=0
while n:
    if n%4==0: cnt+=1
    n//=4
print(cnt)