#Na vstupu je zadána vzestupně uspořádaná posloupnost x_1...x_N
#a čísla y_1...y_M 
#Zařaďte čísla y_i na správná místa do posloupnosti.

N=int(input())
R=N
seznam1=[]
while N!=0:
    x=int(input())
    N=N-1
    seznam1.append(x)
M=int(input())
K=M
seznam2=[]
while M!=0:
    y=int(input())
    M=M-1
    seznam2.append(y)
for j in range(len(seznam2)):
    for i in range (len(seznam1)):
        if(seznam2[j]<=seznam1[i]):
            seznam1.insert(i, seznam2[j])
            break
        elif(seznam2[j]>seznam1[-1]):
           seznam1.append(seznam2[j])
for i in range(len(seznam1)):
    print(seznam1[i])

    
