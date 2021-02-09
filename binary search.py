A=[]
l=len(A)
mi=A[0]
ma=A[l-1]
x=int(1)#サーチ対象
if x<mi or x>ma:
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

