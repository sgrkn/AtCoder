n,k,q=map(int,input().split())
a=list(map(int,input().split()))
l=list(map(int,input().split()))

s=[0]*(n+1)

for i in range(k):
    s[a[i]]=1

for i in range(q):
    count=0

    for now in range(1,n+1):
        if s[now]==1:
            count+=1
        if count==l[i]:
            if now<n and s[now+1]==0:
                s[now+1]=1
                s[now]=0
                break

ans=[]

for i in range(1,n+1):
    if s[i]==1:
        ans.append(i)

print(*ans)