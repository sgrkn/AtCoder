n = int(input())

ans = ""

while 0<n:
    if n%2==0:
        ans+="B"+ans
        n//=2

    else:
        ans="A"+ans
        n-=1

print(ans)