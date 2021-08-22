# Knuth-Morris-Pratt法 
# 照合が失敗した時点の状況（何⽂字⽬まで照合したか）に応じて，次の照合位置を変更
# テーブルにはどこで照合失敗したらどこから照合し直すかが記載
# 照合対象の⽂字列の⻑さがn，照合パターンの⻑さがl
# スキップテーブルの作成：l．照合：最悪でもn よって，O(n+l)

def kmp(S,T):
    table=[0]*(len(T)+1) # スキップテーブル
    table[0] = -1 # 使わない
    i,j = 0,1 # パターン内の繰り返しを調べる
    while j < len(T): # スキップテーブルを作る
        if T[i] != T[j] and i > 0:
            i = table[i]
        else:
            if T[i] == T[j]:
                i += 1
            j += 1
            table[j] = i

    k = l = 0 # テキストとパターンのカーソル位置
    while k < len(S) and l < len(T): # 照合を⾏うループ
        if S[k] == T[l]: # ⼀致している場合は両⽅のカーソルを進める
            k += 1
            l += 1
        elif l == 0:# 照合パターン1⽂字⽬で失敗した場合は，テキスト側のカーソルを1つすすめるだけ．
            k += 1
        else: # 照合パターン2⽂字⽬以降はスキップテーブルを使ってどこから照合し直すか決定
            l = table[l]

    if l == len(T):
        print(k-l)
    else:
        print(-1)

S = 'asdfdgdfhfdhafdgdhfdhd'
T = 'ababd'
kmp(S,T)