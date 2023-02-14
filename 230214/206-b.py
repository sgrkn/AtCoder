n=int(input())

money=0

for i in range(10000000):
    money+=i
    if money>=n:
        print(i)