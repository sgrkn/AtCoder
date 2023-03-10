x1, y1 = list(map(int,input().split()))
x2, y2 = list(map(int,input().split()))
x3, y3 = list(map(int,input().split()))

ans =[]

if x1 == x2:
    ans.append(x3)
elif x1 == x3:
    ans.append(x2)
elif x2 == x3:
    ans.append(x1)

if y1 == y2:
    ans.append(y3)
elif y1 == y3:
    ans.append(y2)
elif y2 == y3:
    ans.append(y1)

print(*ans)