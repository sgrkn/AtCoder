n=int(input())
a=list(map(int,input().split()))
sorted_a=sorted(a)

n_list=[]
for i in range(n):
    n_list.append(i+1)

if sorted_a == n_list:
    print('Yes')

else:
    print('No')