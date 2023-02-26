n = int(input())

for _ in range(n):
    k_a = [int(i) for i in input().split()]
    k = k_a[0]
    a = k_a[1:]
    ans = 0
    for i in range(k):
        ans += a[i]
    print(ans)
