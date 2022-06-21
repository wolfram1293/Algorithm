import time
import matplotlib.pyplot as plt

def fuga(n): # 各桁(10** n) の7がつく数字の数をカウントする(よりシンプル)
    n = list(str(n))
    n = [int(v) for v in n]
    hoge = [0] * len(n)
    digit = 0 # 今処理している桁
    for i in range(len(n)): # 場合の数を使う実装(10**nまでの7がつく数字の数 = 全体(10**n) - どの桁にも7がつかない数字の数(9**n))
        if i != 0:
            hoge[-(i+1)] = int(10**(digit)) - int(9**(digit))
        digit += 1
    return hoge

def cntseven(n): # nまでの7がつく数字の数をカウントする
    ans = 0
    hoge = fuga(n) # 各桁(10** n) の7がつく数字の数をカウント
    n = list(str(n))
    n = [int(v) for v in n]
    flag = False # 桁に7がつくフラグ
    
    digit = len(n)
    for i in range(len(n)):
        d = n[i]
        digit -= 1

        if flag: # 1度でも7がつく桁があれば、それ以降の数字分7がつく数字があるので足して終了
            ans += int(''.join(map(str, n[i:]))) + 1
            break
        elif i == len(n) - 1: # 1桁目ならば、7以上なら +1
            if d >= 7:
                ans += 1
        else: # それ以外なら
            if d == 7: # 7ならフラグを立てその桁の7がつく数字の数 * 桁の数字 を足す
                flag = True
                ans += d * hoge[i]
            elif d < 7: # 7未満ならその桁の7がつく数字の数 * 桁の数字 を足す
                ans += d * hoge[i]
            else: # 8以上ならその桁の7がつく数字の数 * (桁の数字-1) + 10**digit を足す
                ans += (d-1) * hoge[i] + int(10**digit)

    return ans

x = [i for i in range(1, 200)]
y = []
for i in x:
    time_sta = time.perf_counter()
    n = int(10**i)
    cntseven(n)

    time_end = time.perf_counter()
    d = time_end- time_sta
    y.append(d)
    #print(d)


print(y)

'''
plt.figure()
plt.plot(x, y)
plt.show()
'''
