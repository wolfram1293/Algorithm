def solution(A):
    # write your code in Python 3.6
    A.sort()
    N = len(A) # いらんかった
    ans = 1
    for a in A:
        if a == ans:
            ans += 1
        elif a > ans:
            break
            
    return ans

# 1以上の整数で配列の中にない最小のものを探す 多分これが一番簡潔
