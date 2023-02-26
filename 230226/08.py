n,k = map(int,input().split())
a = [[int(i) for i in input().split()]for _ in range(n)]

for i in range(n):
    ans=0
    for j in range(k):
        ans+=a[i][j]
    print(ans)