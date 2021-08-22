#Rabin-Karp法
# 部分⽂字列をハッシュに変換しておき，⽂字列の照合をハッシュ値の⼀致の問題へと変換
# 照合パターンのハッシュ化： O(l) ハッシュを⽤いての照合：⼀番最初だけはO(l)，あとはO(1) ．最悪の場合はn-l回の⽐較が必要．よって，O(n)
# よって，O(n+l)
def RollingHashMatch(S,T):
    a = 1007 # 基数
    h = 10**9+7 # 除数
    Slen = len(S)
    Tlen = len(T)
    Shash = 0 # 照合対象側のハッシュ
    Thash = 0 # 照合パターン側のハッシュ
    num = lambda c : ord(c)-ord('a') # アルファベットを整数に変換
    am = 1
    for i in range(Tlen):
        Shash += num(S[Tlen-i-1])*am
        Thash += num(T[Tlen-i-1])*am
        am *= a
        am %= h
    Shash %= h
    Thash %= h

    for i in range(Slen-Tlen+1):
        if i != 0:
            Shash = (a*Shash+num(S[Tlen+i-1])-am*num(S[i-1])) % h
        if Shash == Thash:
            return i
    
    return -1

S = 'asdfdgdfhfdhafdgdhfdhd'
T = 'fdgd'
RollingHashMatch(S,T)