def binary_search(A,x):
    l = len(A)
    A.sort()
    mi = A[0]
    ma = A[l-1]
    
    if x < mi or x > ma:
        print("No")
    else:
        low=0
        high=l-1
        f=0
        while low<=high:
            mid=(low+high)//2
            if x==A[mid]:
                f=1
                break
            if x>A[mid]:
                low=mid+1
            else:
                high=mid-1
        if f==1:
            print("Yes")
        else:
            print("No")


A = [1,2,4,3,5,2,6,8,2,4,9]
x = 3 #サーチ対象

binary_search(A,x)
