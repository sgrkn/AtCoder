# 二次元配列の行ごとの和
n,k = map(int,input().split())
a = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    s = 0
    for j in range(k):
        s+=a[i][j]
    print(s)