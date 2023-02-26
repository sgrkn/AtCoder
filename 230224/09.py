# さまざまな長さの配列の和
n = int(input())

for _ in range(n):
    k_a = [int(i) for i in input().split()] # 配列のサイズKとその要素 A1 ... AK をリストで受け取る
    k = k_a[0] # 0個目の要素をkに代入
    a = k_a[1:] # 1個目以降の要素をリストaに代入
    s = 0 # 行ごとの和
    for i in range(k):
        s += a[i] # 行ごとの和に各要素を足す
    print(s)