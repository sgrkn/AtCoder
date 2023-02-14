s1=input()
s2=input()
s3=input()
s4=input()

list = ['H','2B','3B','HR']
s_list = [s1, s2, s3, s4]
s_list = set(s_list)
if list==s_list:
    print('Yes')
else:
    print('No')