ans=[]
for N in range(1,10000):
    R = bin(N)[2:]
    if sum(map(int,R)) % 2 == 0:
        R = '11' + R[2:] + '1'
    else:
        if R.count('0') > R.count('1'):
            R += '0'
        else:
            R += '1'
    if int(R,2)>271:
        ans.append(N)
print(min(ans))
