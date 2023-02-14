n=int(input())
a=list(map(int,input().split()))

ans=0

for i in range(n):
    if n>10:
        ans+=n-10
    
print(ans)