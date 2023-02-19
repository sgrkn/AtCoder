x=list(map(int,input().split('.')))
if 0<=x[1]<=2:
    print(x[0]+'-')
elif 3<=x[1]<=6:
    print(x[0])
if 7<=x[1]<=9:
    print(x[0]+'+')
