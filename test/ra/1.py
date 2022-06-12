def solution(A, B, C):
    # write your code in Python 3.6
    l = [[A,'a'], [B,'b'], [C,'c']]
    l.sort(reverse=True)
    ans = ''
    if l[0][0] // 2 + 1 > l[1][0] + l[2][0]:
        while True:
            for i in range(2):
                if l[0][0] == 0:
                    break
                ans += l[0][1]
                l[0][0] -= 1
            
            if l[1][0] > 0:
                ans += l[1][1]
                l[1][0] -= 1
                continue

            elif l[2][0] > 0:
                ans += l[2][1]
                l[2][0] -= 1
                continue

            else:
                break

    elif l[0][0] // 2 + 1  > l[1][0] // 2 + 1  + l[2][0]:
        while True:
            for i in range(2):
                if l[0][0] == 0:
                    break
                ans += l[0][1]
                l[0][0] -= 1

            for i in range(2):
                if l[1][0] == 0:
                    break
                ans += l[1][1]
                l[1][0] -= 1
            
            if l[2][0] > 0:
                ans += l[2][1]
                l[2][0] -= 1
                continue

            else:
                break
    
    elif l[0][0] > l[1][0] + l[2][0]:
        while True:
            for i in range(1):
                if l[0][0] == 0:
                    break
                ans += l[0][1]
                l[0][0] -= 1
            
            if l[1][0] > 0:
                ans += l[1][1]
                l[1][0] -= 1
                continue

            elif l[2][0] > 0:
                ans += l[2][1]
                l[2][0] -= 1
                continue

            else:
                break


    return ans

'''
ABCでabcそれぞれのアルファベットの数が与えられ、各アルファベット2回まで連続していいとしたとき、並べられる最大となるもの(複数ありうる)の一つを出力
場合分けが網羅できなかった。
'''