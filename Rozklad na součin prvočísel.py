
n= int(input())
d=2
if n>=2 and n<=1000000:
 while d<=n:
     if n%d==0:
      print(d)
      n//=d
      while n%d==0:
        print(d)
        n//=d
      else:
        d+=1
     else:
      d+=1
