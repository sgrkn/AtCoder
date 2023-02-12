n=int(input())
t=input()

direct='east'

now=[0,0]

for i in range(n):
    if t[i]=='S':
        now_x=now[0]
        now_y=now[1]
        # east
        if direct=="East":
            now=[now_x+1,now_y]
        # south
        elif direct=="South":
            now=[now_x,now_y-1]
        # west
        elif direct=="West":
            now=[now_x-1,now_y]
        # north
        elif direct=="North":
            now=[now_x,now_y+1]
    
    else:
        if direct=='east':
            direct='south'
        elif direct=='south':
            direct='west'
        elif direct=='west':
            direct='north'
        elif direct=='north':
            direct='east'

print(now[0],now[1])