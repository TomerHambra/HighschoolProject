import math
r = 1
k = 7
m = k*k//2
for n in range(1,m+1):
    p = math.comb(k*k, n) *math.comb(k*k-n+1,n)
    r += p
print(r)
s = 0
m = k*k-k-k+1
for n in range(2,m+1, 2):
    p = math.comb(m, n) *math.comb(n,n//2) // 2
    print(p)
    s += p
s *= math.comb(k*k-k,k-1)//2
m = k*k-k-k
s2 = 0
for n in range(2,m+1, 2):
    p = math.comb(m, n) *math.comb(n,n//2) //2
    print(p, n)
    s2 += p
s2 *= math.comb(k*k-k,k-1)
s+=s2
r -= s*(k**k)
print("res: ")
print(r)
print("upper: ")
print(3**49)