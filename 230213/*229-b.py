def judge():
    a,b=map(int,input().split())
    x,y=a.zfill(20), b.zfill(20)
    for x,y in zip(x,y):
        if int(x)+int(y)>=10:
            return 'Hard'
    return 'Easy'

print(judge())