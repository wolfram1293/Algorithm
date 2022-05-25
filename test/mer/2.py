def minStart(arr):
    # Write your code here
    N = len(arr)
    l = []
    l.append(arr[0])
    for i in range(1, N):
        l.append(l[i-1] + arr[i])
    ans = -min(l) + 1 if min(l) < 0 else 1
    return ans

'''
arrの中の整数を一つずつ足していったとき、そのすべてが1以上になる最小の整数x
lに整数を一つずつ足していった値を入れ、その最低値のときでも1になるようにxを決める
'''