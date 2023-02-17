x=str(input())
ans=x
for i in range(len(x)):
    if x[i]=='.':
        ans=x[:i]
        break
print(ans)