s,k = map(str,input().split())

k = int(input())

s_set = set()

import itertools

#p=(0,1,2), (0,2,1), (1,0,2), (1,2,0), ....
for p in itertools.permutations(range(len(s))):
    stmp = ""
    for i in p:
        stmp+=s[i]

    s_set.add(stmp)

slist = list(s_set)

slist.sort()

print(slist[k-1])


