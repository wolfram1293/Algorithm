# osa_k法
# 前処理の計算量はエラトステネスのふるいと同じO(N log logN)
# 本計算の計算量は素因数の個数に比例．Mの素因数の個数はlogM程度より，計算量もO(logM)
# Mが最大の場合(M=Nの場合)計算量O(logN)より，N以下の正の整数全てを素因数分解する場合も計算量はO(N logN)程度
def osa_k(n):
    # エラトステネスのふるいの応用
    min_factor = [-1] * (n+1) # iの最小の素因数(iを割り切る最小の素数)を格納する配列
    min_factor[0] = 0
    min_factor[1] = 1
    for i in range(2, n+1):
        if min_factor[i] == -1: # 素数なら
            min_factor[i] = i # min_factor[i] = iとして
            for j in range(i*i, n+1, i): # i*i以上のiの倍数jに対し
                if min_factor[j] == -1: # jがまだmin_factorを持たないならmin_factor[j] = iとする
                    min_factor[j] = i
    
    ans = [1] if n == 1 else []
    k = n
    while k > 1: # 1になるまでkをmin_factor[k]で割ってkを更新
        ans.append(min_factor[k])
        k //= min_factor[k]
    
    return ans

N = 12
ans =[]
for i in range(N):
    ans.append(osa_k(i+1))
print(ans)
