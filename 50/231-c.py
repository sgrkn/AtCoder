n,q = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

def nibutan(x):
    l = 0
    r = n-1

    while 1<r-1:
        c = (l+r)//2

        if a[c]<x:
            l=c
        else:
            r=c

    return r

for i in range(q):
    x = int(input())

    if x<=a[0]:
        print(n)
    elif a[n-1]<x:
        print(0)
    else:
        print(n-nibutan(x))
        