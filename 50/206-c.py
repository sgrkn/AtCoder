n = int(input())
a = list(map(int,input().split()))

from collections import defaultdict

count = defaultdict(int)

for i in range(n):
    count[a[i]]+=1

ans = n*(n-1)//2

for x in count.values():
    ans-=x*(x-1)//2

print(ans)