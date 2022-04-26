# マージソート
# まず再帰で2分割を繰り返して、戻りながら小さい順にマージ
# 分割するときは何も考えない 結合するときにソートする
# ⼀般ケース, 最悪ケースともにO(n log n) 
def mergesort(seq):
    if len(seq) <= 1: return seq
    # 2つに分割するだけ
    left = mergesort(seq[:len(seq)//2])
    right = mergesort(seq[len(seq)//2:])
    # これらの値が返ってきたときには，left，right
    # 各々でソートができている状態になっている．
    merged = []
    cur_l = cur_r = 0
    # マージ作業．⼩さい⽅から順にmergedに⼊れる．
    while cur_l < len(left) and cur_r < len(right):
        if left[cur_l] <= right[cur_r]: # 安定性を確保
            merged.append(left[cur_l])
            cur_l += 1
        else:
            merged.append(right[cur_r])
            cur_r += 1
    # もし余った要素があればくっつける．
    if cur_l < len(left):
        merged.extend(left[cur_l:])
    elif cur_r < len(right):
        merged.extend(right[cur_r:])
    return merged

A = [3,5,6,8,3,2,1,4,6,7,0,5,9]
mergesort(A)