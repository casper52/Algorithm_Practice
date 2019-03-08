
def gcd(a,b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

print(gcd(60,24))

def euclid_gcd(a,b):
    if b == 0:
        return a
    return euclid_gcd(b, a % b)

print(euclid_gcd(60,24))

def fibo(n):
    if n < 2 :
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(2))