import sys
import requests
import json
# 漸化式の一部にAPIのリターンが入る (指定？により)再帰で実装
def f(n, table):
    if table[n] == 0:
        if n == 0:
            table[n] = 1
        elif n == 2:
            table[n] = 2
        elif n % 2 == 0:
            table[n] = f(n-1, table) + f(n-2, table) + f(n-3, table) + f(n-4, table)
        else:
            table[n] = askServer(n)

    return table[n]

def askServer(n):
    endpoint = 'http://challenge-server.code-check.io/api/recursive/ask'
    payload = {"seed": seed,"n": n}
    r = requests.get(endpoint, params=payload).json()['result']
    return r

argv = sys.argv
if len(argv) == 3:
    try:
        seed = argv[1]
        n = int(argv[2])
    except:
        print('Error2')
        sys.exit(1)
else:
    print('Error1')
    sys.exit(1)

table = [0] * (n+1)
print(f(n, table))

# 漸化式方式
def f(n):
    table = [0] * (n+1)
    for i in range(n+1):
        if i == 0:
            table[i] = 1
        elif i == 2:
            table[i] = 2
        elif i % 2 == 0:
            table[i] = table[i-1] + table[i-2]  + table[i-3]  + table[i-4]
        else:
            table[i] = askServer(i)

    return table[n]
    