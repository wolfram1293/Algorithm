W = 15
N = 6
weight = [11, 2, 3, 4, 1, 5]
value = [15, 3, 1, 4, 2, 8]

def knapsack2(N,W): # 漸化式方式
    note = [[-1 for i in range(W+1)] for j in range(N+1)] # インデックスはアイテム番号、重さと同じ(最初の行、列は0番目のアイテム、重さ0の時を表す)
    for i in range(W+1): # 「0」の⾏のセルは全部0で初期化
        note[0][i] = 0

    for i in range(1,N+1): # 1からN番目のアイテムまで
        for w in range(W+1): # 重さ0からWまで
            if w < weight[i-1]: # 重さwがi番目のアイテムの重さより小さいとき
                note[i][w]=note[i-1][w] # i番目のアイテムは入らないので重さwでi-1番目のアイテムまで考えたとき(note[i-1][w])をnoteに入れる
            else: # 重さwがi番目のアイテムの重さ以上のとき
                note[i][w]= max(note[i-1][w-weight[i-1]] + value[i-1], note[i-1][w]) # 重さwでi-1番目のアイテムまで考えたときとi番目のアイテムを考えたときを比較し、大きい方をnoteに入れる
    
    return note

print(knapsack2(N,W)[N][W])
