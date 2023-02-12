n=int(input())
a=list(map(int,input().split()))

count=[0]*(n+1)

for i in range(4*n-1):
    count[a[i]]+=1

for i in range(1,n+1):
    if count[i]==3:
        print(i)
        exit()
