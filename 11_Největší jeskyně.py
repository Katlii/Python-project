#Na mapě chceme najít největší jeskyni (co do počtu políček) a její těžiště: 
#políčko s průměrnou řádkovou a sloupcovou souřadnicí ze všech políček jeskyně (zaokrouhleno dolů). 
#Slibujeme, že ve všech testovacích vstupech bude taková jeskyně jednoznačně určena.

#Formát vstupu: Na standardním vstupu je mapa jeskynního systému: 
#RR řádků po SS znacích. Každý znak popisuje jedno políčko mapy: . pro volné políčko, # pro skálu.

#Formát výstupu: Vypište jeden řádek se třemi čísly oddělenými mezerou: 
#počet políček v největší jeskyni, řádkovou souřadnici těžiště a sloupcovou souřadnici těžiště (políčko (0,0)(0,0) je vlevo nahoře).

import sys
from typing import List
a =[]
for symbol in sys.stdin:
    a.append(list(symbol.strip()))

for i in range(len(a)):
    for j in range (len(a[0])):
        if a[i][j]=='.': a[i][j]=0
        if a[i][j]=='#': a[i][j]=1

def jeskyni(matrix: List[List[int]]) -> List[int]:
    def check(x: int, y: int, count: int) -> int:
        combinations.add((x, y))
        teziste1.append(x)
        teziste2.append(y)
        count += 1
        if x - 1 >= 0 and matrix[x - 1][y] == 0 and (x - 1, y) not in combinations:
            
            return check(x - 1, y, count)
        if x + 1 < len(matrix) and matrix[x + 1][y] == 0 and (x + 1, y) not in combinations:
           
            return check(x + 1, y, count)
        if y - 1 >= 0 and matrix[x][y - 1] == 0 and (x, y - 1) not in combinations:
            
            return check(x, y - 1, count)
        if y + 1 < len(matrix[0]) and matrix[x][y + 1] == 0 and (x, y + 1) not in combinations:
            
            return check(x, y + 1, count)
        return count
 
    
    combinations = set()
    teziste1=[]
    teziste2=[]
    counts = []
    for line_index, line in enumerate(matrix):
        for el_index, element in enumerate(line):
            #if line_index==0:
                if element == 0 and (line_index, el_index) not in combinations:
                    total_count = check(line_index, el_index, 0)
                    counts.append(total_count)
    for i in range(len(counts)-1):
        counts.remove(min(counts))
    
    counts.append(0)
    counts.append(0)
    for i in range(counts[0]):
        counts[1]=counts[1]+teziste1[i]
    for j in range(counts[0]):
        counts[2]=counts[2]+teziste2[j]
    if counts[0]!=0:
        counts[1]=counts[1]//counts[0]
        counts[2]=counts[2]//counts[0]

    return counts

b=jeskyni(a)
print(*(b))
           
               
                        
            
