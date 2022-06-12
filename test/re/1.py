import sys
# mをaで割ったあまり0なら文字列加える？みたいなやつ
raw = input().split()
l = []
for v in raw[:-1]:
    a, s = v.split(':')
    l.append([int(a), s])

m = int(raw[-1])
l.sort()
ans = ''
for v in l:
    a, s = v[0], v[1]
    if m % a == 0:
        ans += s

if ans == '':
    print(m)
else:
    print(ans)
