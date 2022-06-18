import sys
def seven(day):
    day = list(str(day))
    day = [int(v) for v in day]
    if 7 in day:
        return True
    else:
        return False

def cntseven(day):
    ans = 0
    i = 0
    while True:
        if day == 0:
            break
        remainder = day % 10
        if remainder >= 7:
            ans += 1
        day = (day - remainder) / 10
        ans += (10 ** i) *day
        i += 1
    
    return ans

a, b, n = map(int, input().split())
point = 0
day = 0

day1 = n // a

while True:
    point += a
    if seven(day):
        point += b
    if point >= n:
        break

    day += 1

print(day)

'''
7がつく日がポイント加算される店のポイントを規定以上貯める問題
最初はナイーブに1日ずつカウントを進めていき、7のつく日とそれ以外で分け、ポイントを足していく方針で実装した。
計算量は7のつく日の判定はO(日付の桁数)より、高々O(log(n))、日を進めていくカウントはO(かかる日数)より、高々O(n)、よって全体では高々O(n log(n))である。

しかし、これで実行制限時間に引っかかったため、高速化を考えた。
次に7がつく日付の判定をO(1)とし、全体の計算量O(n)としたが、実行時間が足りなかったため、それ以上の高速化を考えた。

かかる日数は高々int(n/a)より、その中の7がつく日の数をカウントして、かかる日数をそれから逆算的に引いていく方法を実装しようとしたが実装が間に合わなかった。
'''
