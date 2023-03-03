n = int(input())

mountains = []

for i in range(n):
    s,t = map(str, input().split())
    t = int(t)
    mountains.append([t,s])

mountains.sort(reverse=True)

print(mountains[1][1])