n = int(input())

used = [False]*(2*n+2)

print(1)

used[1]=True

for i in range(n+1):
    x = int(input())
    used[x]=True

    if x==0:
        exit()

    for k in range(1,2*n+2):
        if used[k]==False:
            print(k)
            used[k]=True
            break