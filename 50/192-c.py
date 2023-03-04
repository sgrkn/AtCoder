n = int(input())
a = list(map(int,input().split()))
x = int(input())

asum = sum(a)

quo = a//asum

k = n*quo

bsum = asum*quo

for i in range(n):
    bsum+=a[i]
    k += 1

    if x<bsum:
        print(k)
        exit()