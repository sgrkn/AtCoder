h,w=map(int,input().split())
a=[]

for i in range(h):
    a_tmp=list(map(int,input().split()))
    a.append(a_tmp)

b=[[0]*h for i in range(w)]

for i in range(w):
    for j in range(h):
        b[i][j]=a[j][i]

for i in range(w):
    print(*b[i])