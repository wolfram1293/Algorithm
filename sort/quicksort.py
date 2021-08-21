# クイックソート
# 軸より大小で2分割して再帰
# 分割するときに（ざっくり）ソートする 結合するときは何も考えない
# ⼀般ケースO(n log n) 最悪ケースO(n^2)
def quicksort(seq):
    if len(seq) <= 1:
        return seq

    left = []
    right = []
    pivot = seq[len(seq)//2] # 枢軸の選び方(ランダムだと最悪ケースに対応しやすい)
    count = 0
    for i in range(len(seq)):
        e = seq[i]
        if e == pivot:
            count += 1
        elif e < pivot:
            left.append(e)
        else:
            right.append(e)
            
    left = quicksort(left)
    right = quicksort(right)
    return left + [pivot]*count + right

A = [3,5,6,8,3,2,1,4,6,7,0,5,9]
quicksort(A)