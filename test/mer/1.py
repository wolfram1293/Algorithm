def theFinalProblem(target):
    # Write your code here
    target = [int(n) for n in list(target)]
    N = len(target)
    ans = 0
    for i in range(N):
        if target[i] == 1:
            if ans % 2 == 0:
                ans += 1
        else:
            if ans % 2 == 1:
                ans += 1
                
    return ans 

'''
選択した桁以下のバイナリ反転
上の桁から順に見ていき、反転回数の偶奇で反転するか判定
'''