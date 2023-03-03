n = int(input())
a = list(map(int,input().split()))

a_2 = []

for i in range(n):
    if a[i] not in a_2:
        a_2.append(a[i])

print(len(a_2))