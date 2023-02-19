k=int(input())
a,b=map(int,input().split())
for i in range(a,b+1): 
  if i%k==0:
    print('OK')
    exit()
else:
    print('NG')

"""
range(1,5)

first - 1
last - 4
end - 5

実際ループするのはlastまで
"""