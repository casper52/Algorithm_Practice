#동명이인 찾아서 집합으로 출력하기

def find_samaname(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["Jay", "Johnny", "Mark", "Jay" ,"Mark"]



#짝을 지을 수 있는 모든 조합 출력하기

def set_pair(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
           print(a[i],'-',a[j])

name= ["Tom","Jerry","Mike"]
set_pair(name)
print()
name2=["Tom","Jerry","Mike","John"]
set_pair(name2)
