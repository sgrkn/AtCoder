# 二次元配列の出力

n,k = map(int,input().split())
a = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(k):
        if j == k-1:
            print(a[i][j])
        else:
            print(a[i][j], end=' ')