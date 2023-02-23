# 指定された範囲・行数の数字の出力
n,k = map(int,input().split())
for _ in range(k): # 1〜Nの数字を空白区切りで順に出力する操作をK回繰り返す
    for i in range(1, n+1): 
        if i == n: 
            print(i) #Nを出力する場合は、数字の後ろに改行を出力する。"N"を出力したのち改行することができる。
        else:
            print(i, end=" ") # 1 〜 (N-1) を出力する場合は、数字の後ろに半角スペースを出力する