m,n=map(int,input().split())
k,r=map(int,input().split())
o,a=map(int,input().split())
if (((m==k) and(k==o))or((n==r)and(r==a))):
  print("yes")
elif((m==n) and(k==r)and (o==a)): 
  print("yes")
else:
  print("no")


