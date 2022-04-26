# シェーカーソート
# 最悪計算量はこちらもO(n^2) ただし，バブルソートよりはちょっと速いことが期待できる
def shakersort(seq):
    # ソート済みの左端，右端を保持する変数
    left = 0
    right = len(seq) - 1
    # 最後にスワップが起きた場所を格納する変数
    swapped = 0
    while left < right:
        for i in range(left, right): # 先頭からチェック
            if seq[i+1] < seq[i]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swapped = i
        # 最後のスワップの場所でrightを更新
        right = swapped

        for i in range(right, left, -1): # 次は後ろからチェック
            if seq[i] < seq[i-1]:
                seq[i], seq[i-1] = seq[i-1], seq[i]
                swapped = i
        # 最後のスワップの場所でleftを更新
        left = swapped
    
    return seq

A = [3,5,6,8,3,2,1,4,6,7,0,5,9]
shakersort(A)