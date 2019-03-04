#1~n까지의 합

def sum(n):
    s = 0
    for i in range(1,n+1):
        s = s + i
    return s

print(sum(10))

def sum2(n):
    return  n * ( n + 1 ) // 2

print(sum2(100))

# 1~n까지 제곱의 합
def sum3(n):
    s = 0
    for i in range (1, n+1):
        s = s + i**2
    return s

print(sum3(10))

def sum4(n):
    return n*(n+1)*((2*n)+1) // 6

print(sum4(10))