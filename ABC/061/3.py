S = input()
l = len(S) - 1
ans=0
for i in range(2 ** l):
    op = ["-"] * l
    for j in range(l):
        if ((i >> j) & 1):
            op[l - 1 - j] = "+"
    formula = ""
    for j in range(l):
        formula+=S[j]
        if op[j]=="+":
            formula+="+"
    formula+=S[l]
    ans+= eval(formula)
print(ans)
