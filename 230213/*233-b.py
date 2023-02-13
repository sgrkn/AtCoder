l,r = map(int,input().split())
s=input()

s_list=list(s)
s_left=s_list[l-1]
s_center=s_list[l-1:r]
s_right=s_list[r:]

s_center=s_center[::-1]
s=s_left+s_center+s_right

s_join="".join(s)

print(s_join)