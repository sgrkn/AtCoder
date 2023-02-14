n = int(input())
a = list(map(int,input().split()))

a_sorted = sorted(a)
ans=a_sorted[-2]
print(a.index(ans)+1)