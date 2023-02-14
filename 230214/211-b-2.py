S = []
for i in range(4):
    S.append(input())
cnt = 0
# for i in ['H', '2B', '3B', 'HR']:
#     cnt += (int)(i in S)
# print('Yes' if cnt == 4 else 'No')

for i in S:
    if i == 'H' or i == '3B' or i == '2B' or i == 'HR':
        cnt += 1

if cnt == 4:
    print('Yes')
else:
    print('No')