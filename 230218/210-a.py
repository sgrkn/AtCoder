n,a,x,y=map(int,input().split())
money=0
for i in range(n):
    if i<=a:
        money+=x
    elif i>a:
        money+=y
print(money)