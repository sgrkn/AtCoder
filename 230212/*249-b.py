def judge():
    s=input()
    b1=not s.islower()
    b2=not s.isupper()
    #すべての文字が異なるならば文字列Sに現れる文字の種類数と文字列Sの長さは等しい
    b3=len(s)==len(set(s))
    return b1 and b2 and b3

print('Yes' if judge() else 'No')