W = 15
N = 6
weight = [11, 2, 3, 4, 1, 5]
value = [15, 3, 1, 4, 2, 8]
note = [[-1 for i in range(W+1)] for j in range(N+1)] # インデックスはアイテム番号、重さと同じ(最初の行、列は0番目のアイテム、重さ0の時を表す)

def knapsack1(i, w): # メモ化再帰
    if note[i][w] != -1: # noteがあれば
        return note[i][w] # noteから値を返す
    # noteが空のとき
    if i == 0: # 0番目のアイテムのとき(1つもアイテムが入っていないとき)
        note[i][w] = 0 # noteに0を入れて返す
        return note[i][w]
    elif w < weight[i-1]: # wがi番目のアイテムの重さより小さいとき
        note[i][w] = knapsack1(i-1, w) # noteにknapsack1(i-1, w)(重さwでi-1番目のアイテムまで考えたとき)を入れて返す
        return note[i][w]
    else: # それ以外のとき(wがi番目のアイテムの重さ以上で入れる可能性があるとき)
        note[i][w] = max(knapsack1(i-1, w), knapsack1(i-1, w-weight[i-1]) + value[i-1]) # noteに重さwでi-1番目のアイテムまで考えたときとi番目のアイテムを考えたときを比較し、大きい方を入れて返す
        return note[i][w]

knapsack1(N, W)
print(note[N][W])
