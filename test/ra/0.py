def solution(A):
    # write your code in Python 3.6
    A.sort()
    N = len(A)
    ans = 1
    for a in A:
        if a == ans:
            ans += 1
        elif a > ans:
            break
            
    return ans
