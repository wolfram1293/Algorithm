def solve(S,C,K):
  # Write your solution here.
  #
  # Warning: Printing unwanted or ill-formatted data to output will cause
  # the test cases to fail.
  front,back=0,0
  cnt=0
  ans=-1
  for i in range(len(S)):
    if S[i]==C:
      cnt+=1
    if cnt==K:
      back=i
      ans=i+1
      break
  
  if ans!=-1:
    mode=0
    while True:
      if back>=len(S):
        break
      if mode==0:
        if S[front]==C:
          ans=min(ans,back-front+1)
          back+=1
          mode=1 
        else:
          front+=1
      else:
        if S[back]==C:
          front+=1
          mode=0
        else:
          back+=1
          
  return ans
