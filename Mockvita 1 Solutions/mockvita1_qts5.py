def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def mullnv(s):
    import math
    a = 1000000007
    a = math.ceil(a / s)
    return a

def gcd(v,w):
    if(v==0 or w==0):
        return 0
    if(v==w):
        return v
    if(v > w):
        return gcd(v-w,w)
    return gcd(v,w-v)

from fractions import Fraction
t = int(input())
if t>0 and t<=1000:
    for j in range(t):
        a = input()
        a = a.split(" ")
        N = int(a[0])
        T = int(a[1])
        M = int(a[2])
        if N>0 and N<=1000:
            if T>0 and T<=1000:
                if M>=0 and M <= 1000:
                    if M<=N and T<=N:
                        p = factorial(T) * factorial(N-M)
                        q = factorial(N) * factorial(T-M)
                        k = Fraction(p,q).numerator
                        l = Fraction(p,q).denominator
                        if gcd(k,l)==1:
                            print(k * mullnv(l))
