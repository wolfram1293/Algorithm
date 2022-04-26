# 挿⼊ソート
# 1回の平均的な⽐較・移動回数はそれぞれi/2．それをn-1回繰り返す．最後はn番⽬の要素を，最⼤n-1回⽐較・移動する O(n^2)
def insertionsort(seq):
    for i in range(1, len(seq)):
        j = i - 1
        tmp = seq[i]
        while seq[j] > tmp and j > -1:
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = tmp
    return seq

A = [3,5,6,8,3,2,1,4,6,7,0,5,9]
insertionsort(A)