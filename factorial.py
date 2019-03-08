
def factorial(num):
    f = 1
    for i in range (1,num+1):
        f = f * i
    return f

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(5))

# 반복문이나 재귀호출 이용한 알고리즘의 계산복잡도는 모두 O(n)이다

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print(sum(100))

def find_max(a, n):
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n-1)
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]

v = [17,92,18,33,58,7,33,42]
print(find_max(v,len(v)))
