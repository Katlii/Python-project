#In the sequence of integers,
#find and write out the second largest value.
#The sequence always contains at least two different values, and the numbers can be repeated arbitrarily. All numbers are written on one line at the input and are separated by spaces.

#Note: distinguish the rainbow largest number and the second largest value.

#Example: if there is a sequence of 4 5 1 4 5 3 at the input, the correct result will be the number 4.

#DO NOT USE .SORT(REVERSE=TRUE)
seznam=[]
max=0
index_dva=0     #index of the second largest value
for x in input().split():
    seznam.append(int(x))
seznam.sort()
lenght=len(seznam)
index=lenght-1     #index of the first largest value
index_dva=index
for i in range(index,0, -1):
    if seznam[i]==seznam[i-1]:
       index_dva=i-1
    else:
        max=seznam[index_dva-1]
        break
print(max)
        



