# 指定された数字までの出力
n = int(input())
a = []
for i in range(1, n+1):
    a.append(i)
    
print(*a)