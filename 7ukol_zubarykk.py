# Gauss method (direct)
 
def gauss(A):
    sgn=1
    for r in range(N): # r - reference line number
        z=A[r][r]     # main element
        # iterating through all the lines below r
        if abs(z)<1.0e-10: # zero on the diagonal
           # looking for a non-zero element below 
           for j in range(r+1,N):
               if abs(A[j][r])>1.0e-10:
                   for jj in range(r,N):
                       A[j][jj],A[r][jj]=A[r][jj],A[j][jj]       
                   z=A[r][r]
                   sgn=-sgn
                   break
        for i in range(r+1,N):
            q=A[i][r]/z
            for j in range(N+1):
                A[i][j]=A[i][j]-A[r][j]*q
    return(A, sgn)
 
# Gauss method (reverse)
 
def rev_calc(A):
    global N
    res=[0 for _ in range(N)]
    i=N-1
    if (A[i][i]!=0):
     res[i]=A[i][N]/A[i][i]
     i=i-1
     while(i>=0):
         s=A[i][N]
         for j in range(i+1,N):
             s=s-A[i][j]*res[j]
         res[i]=s/A[i][i]
         i=i-1
     return res    
 
N=int(input())   #how many unknowns
A = [[int(elem) for elem in input().split()] for i in range(N)]
 
res=gauss(A)
arg=rev_calc(res[0])
for i in range(len(arg)):
    print(arg[i])
