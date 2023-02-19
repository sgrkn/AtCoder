a=list(map(int,input().split()))
sorted_a=sorted(a, reverse=True)
print(sum(sorted_a[:2]))