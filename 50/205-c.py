A,B,C = map(int,input().split())
if C % 2 == 0:
  if abs(A) > abs(B):
    print('>')
  if abs(A) == abs(B):
    print('=')
  if abs(A) < abs(B):
    print('<')
else:
  if A > 0 and B > 0:
    if A > B:
      print('>')
    if A == B:
      print('=')
    if A < B:
      print('<')
  if A > 0 and B < 0:
    print('>')
  if A < 0 and B > 0:
    print('<')
  if A < 0 and B < 0:
    if abs(A) > abs(B):
      print('<')
    if abs(A) == abs(B):
      print('=')
    if abs(A) < abs(B):
      print('>')
  if A == 0 and B != 0:
    if B > 0:
      print('<')
    else:
      print('>')
  if A != 0 and B == 0:
    if A > 0:
      print('>')
    else:
      print('<')
  if A == 0 and B == 0:
    print('=')