def seven(day): # 7がつく数字の判定 O(log n)
    day = list(str(day))
    day = [int(v) for v in day]
    if 7 in day:
        return True
    else:
        return False

def fuga0(day): # 各桁(10**n) の7がつく数字の数をカウントする
    day = list(str(day))
    day = [int(v) for v in day]
    hoge = [0] * len(day)
    digit = 0 # 今処理している桁
    for i in range(len(day)): # 漸化式での実装(10**nまでの7がつく数字の数 = 10**(n-1) + 10**(n-1)までの7がつく数字の数 * 9) 
        if i != 0:
            hoge[-(i+1)] = int(10**(digit-1)) + hoge[-i] * 9
        digit += 1
    return hoge

def fuga(day): # 各桁(10** n) の7がつく数字の数をカウントする(よりシンプル)
    day = list(str(day))
    day = [int(v) for v in day]
    hoge = [0] * len(day)
    digit = 0 # 今処理している桁
    for i in range(len(day)): # 場合の数を使う実装(10**nまでの7がつく数字の数 = 全体(10**n) - どの桁にも7がつかない数字の数(9**n))
        if i != 0:
            hoge[-(i+1)] = int(10**(digit)) - int(9**(digit))
        digit += 1
    return hoge

def cntseven(day): # dayまでの7がつく数字の数をカウントする
    ans = 0
    hoge = fuga(day) # 各桁(10** n) の7がつく数字の数をカウント
    day = list(str(day))
    day = [int(v) for v in day]
    flag = False # 桁に7がつくフラグ
    
    digit = len(day)
    for i in range(len(day)):
        d = day[i]
        digit -= 1

        if flag: # 1度でも7がつく桁があれば、それ以降の数字分7がつく数字があるので足して終了
            ans += int(''.join(map(str, day[i:]))) + 1
            break
        elif i == len(day) - 1: # 1桁目ならば、7以上なら +1
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

a, b, n = map(int, input().split())
point = 0
day0 = n // a # 大体の日数のあたりをつける
hoge = fuga(day0)
ratio = hoge[0] / 10 ** (len(list(str(hoge[0])))) # 大体の日数から7のつく日の割合を計算

day = int(n / (a + b * ratio)) # 7のつく日の割合からより正確な日数のあたりをつける

point = a * (day + 1) + b * cntseven(day) # その時のポイントを計算

if point < n: # 目標より低かったら1日ずつ加算
    while True:
        day += 1
        point += a
        if seven(day):
            point += b
        if point >= n:
            print(point)
            break

else:
    while True:
        day -= 1
        point -= a
        if seven(day):
            point -= b
        if point == n:
            break
        elif point < n:
            day += 1
            break

print(day)
