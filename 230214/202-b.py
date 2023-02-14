s=input()
s=s[::-1]
ans=''

for x in s:
    if x=='0':
        ans+='0'
    elif x=='1':
        ans+='1'
    elif x=='6':
        ans+='9'
    elif x=='8':
        ans+='8'
    elif x=='9':
        ans+='6'

print(ans)