s=input()
x1=s[0]
x2=s[1]
x3=s[2]
x4=s[3]

if x1==x2==x3==x4:
    print('Weak')
    exit()

if (int(x1)+1)%10==int(x2) and (int(x2)+1)%10==int(x3) and (int(x3)+1)%10==int(x4):
    print('Weak')
    exit()

print('Strong')