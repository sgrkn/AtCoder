import math
a,b,c,d = map(int,input().split())

if (c*d-b)<=0:
    print(-1)

else:
    ans=math.ceil((a/(c*d-b)))
    print(ans)