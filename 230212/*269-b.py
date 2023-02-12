slist=[]

for i in range(10):
    s=input()
    slist.append(s)

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                ok=True

                for i in range(10):
                    for j in range(10):
                        if a<=i<=b and c<=j<=d:
                            if slist[i][j]==".":
                                ok=False

                        else:
                            if slist[i][j]=='#':
                                ok=False

                if ok==True:
                    print(a+1,b+1)
                    print(c+1,d+1)

                    exit()

