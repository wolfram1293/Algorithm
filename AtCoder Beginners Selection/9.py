import sys
S=input()
a='dream'
b='dreamer'
c='erase'
d='eraser'
while len(S)>0:
  if S.endswith(a):
    S=S[:len(S)-len(a)]
  elif S.endswith(b):
    S=S[:len(S)-len(b)]
  elif S.endswith(c):
    S=S[:len(S)-len(c)]
  elif S.endswith(d):
    S=S[:len(S)-len(d)]
  else:
    print('NO')
    sys.exit()
print('YES')
