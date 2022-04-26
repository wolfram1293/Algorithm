# バケットソート
# 0からmax_valueまでの整数値のみと想定
# バケツの準備：⼀般的にはk．バケツに⼊れる：n．バケツから取り出す：max(n,k)．
# よって，O(n+k)．kがnかそれ以下のオーダーならば，n
def bucketsort(seq, max_value):
    count = [0]*(max_value+1) # バケツ
    sorted = [] # ソート済み配列
    # 出現回数をカウント
    for i in range(len(seq)):
        count[seq[i]] += 1
    # 出現回数からソート済み配列を⽣成
    for i in range(len(count)):
        for j in range(count[i]):
            sorted.append(i)
    return sorted

A = [3,5,6,8,3,2,1,4,6,7,0,5,9]
bucketsort(A,9)