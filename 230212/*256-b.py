n=int(input())
a=list(map(int,input().split()))

p=0

koma=[0]

for i in range(n):
    newkoma=[0]

    for x in koma:
        if x+a[i]<4:
            newkoma.append(x+a[i])
        else:
            p+=1

    koma=newkoma

print(p)