a,b,c,x=map(int,input().split())
if a>=x:
    print(1)
elif a < x <= b:
    print(c/(b-a))
else:
    print(0)
