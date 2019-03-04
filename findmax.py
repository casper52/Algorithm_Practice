#리스트에서 최댓값 찾기

def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1,n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v


def find_maxidx(a):
    n = len(a)
    max_idx = 0

    for i in range(1,n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx


v = [17,92,18,33,58,7,33,42]

print(find_max(v))
print(find_maxidx(v))