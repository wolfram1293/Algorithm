# バブルソート
# O(n^2)
def bubblesort(seq):
    size = len(seq)
    for i in range(size):
        for j in range(size-1, i, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
    return seq

A = [3,5,6,8,3,2,1,4,6,7,0,5,9]
bubblesort(A)