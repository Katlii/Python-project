string=input()
N=int(input())
i=0
string=string.split()
string2=string[0]
for i in range(1, len(string)):
        if (len(string2+string[i])+1)<=N:
          string2=string2+' '+string[i]
        else:
            print(string2)
            string2=string[i]
            continue
        if(len(string2))>N:
           string2=string2.split()
           string2.remove(string2[len(string2)-1])
           print(' '.join(string2))
           string2=string[i]
print(string2)      






