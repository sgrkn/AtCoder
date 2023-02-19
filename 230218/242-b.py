n,m=map(int,input().split())
s=[]

ans=0

for i in range(n):
    s.append(input())

for i in range(n):
  for j in range(i+1,n):
      o_count=0
      for k in range(m):
        if s[i][k]=='o' or s[j][k]=='o':
          o_count+=1
          
      if o_count==m:
        ans+=1

print(ans)
          
"""
n,m=map(int,input().split())
s=[]

ans=0

for i in range(n):
    s.append(input())

for i in range(n):
  for j in range(i,n):
    if i!=j:
      o_count=0
      for k in range(m):
        if s[i][k]=='o' or s[j][k]=='o':
          o_count+=1
          
      if o_count==m:
        ans+=1

print(ans)
          

"""