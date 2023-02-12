h,w=map(int,input().split())
#koma_coordinate
p=[]
for g in range(h):
    s=input()

    for r in range(w):
        if s[r]=='o':
            p.append([g,r])

gmove=abs(p[0][0]-p[1][0])
rmove=abs([[0][1]-p[1][1]])

print(gmove+rmove)