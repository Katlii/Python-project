#Na vstupu jsou dva řádky: první obsahuje text (slova oddělená jednou mezerou), na druhém je číslo W
#Zformátujte text do odstavce s řádky širokými nejvýše W. 
#Na první řádek tedy naskládejte co nejvíce slov tak, aby jejich celková délka včetně mezer mezi nimi nepřesáhla W. 
#Mezery na konci řádku nevypisujte. Pak stejným způsobem vytvořte druhý řádek a tak dále. 
#Pokud se v textu vyskytne slovo o více než WW znacích, pak toto slovo výjimečně může tvořit samostatný řádek.

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






