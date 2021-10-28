seznam = []
max=0
while True:
 x = int(input())
 if x == -1:
  break
 seznam.append(x)
k=int(input())
max=seznam[0]
lenght=len(seznam)
for i in range(lenght-1):
 if max<seznam[i+1]:
     max=seznam[i+1]
if k==1:
    print(max)
else:
 seznam.remove(max)
 max=seznam[0]
 k=k-1
 while k!=0:
  for i in range(len(seznam)-1):
   if max<seznam[i+1]:
       max=seznam[i+1]
  k=k-1
  if k==0:
      print(max)
  else:
   seznam.remove(max)
   max=seznam[0]




