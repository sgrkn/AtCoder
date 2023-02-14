n,k=map(int,input().split())

ans=0

for i in range(n):
    for j in range(k):
       room = str(i)+'0'+str(j)
       print(room)
       ans += int(room)

print(ans)