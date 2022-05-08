#The aim of this task is to practice data visualization using the MatPlotLib python library on historical temperature data 
#measured at the Prague-Klementinum ( https://recodex.mff.cuni.cz/api/v1/uploaded-files/d31299f3-6189-11ea-a595-00505601122b/download ) meteorological station. 
#Write a program that draws the following graphs:

#_Annual average, minimum and maximum temperatures
#_Monthly average, minimum and maximum temperatures (for each month averaged over all years)

import matplotlib.pyplot as plt
import numpy as np
import math
import csv

with open("PKLM.csv", 'r') as file:
    #reader=csv.reader([next(file) for x in range(1000)])
    reader=csv.reader(file)
    count=0
    prumer_list, prumer_min, prumer_max =[], [], []
    rok =[]
    mesic=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    summa_tmp, summa_min, summa_max =0, 0, 0
    remember=1775
    pr_mesic_list, pr_mesic_max, pr_mesic_min=[0]*12, [0]*12, [0]*12

    for row in reader:
        if count==0:
            count+=1
        else:
            if int(row[1])==1:
                    pr_mesic_list[0]=pr_mesic_list[0]+float(row[3])
                    pr_mesic_max[0]=pr_mesic_max[0]+float(row[4])
                    pr_mesic_min[0]=pr_mesic_min[0]+float(row[5])
            if int(row[1])==2:
                    pr_mesic_list[1]=pr_mesic_list[1]+float(row[3])
                    pr_mesic_max[1]=pr_mesic_max[1]+float(row[4])
                    pr_mesic_min[1]=pr_mesic_min[1]+float(row[5])
            if int(row[1])==3:
                    pr_mesic_list[2]=pr_mesic_list[2]+float(row[3])
                    pr_mesic_max[2]=pr_mesic_max[2]+float(row[4])
                    pr_mesic_min[2]=pr_mesic_min[2]+float(row[5])
            if int(row[1])==4:
                    pr_mesic_list[3]=pr_mesic_list[3]+float(row[3])
                    pr_mesic_max[3]=pr_mesic_max[3]+float(row[4])
                    pr_mesic_min[3]=pr_mesic_min[3]+float(row[5])
            if int(row[1])==5:
                    pr_mesic_list[4]=pr_mesic_list[4]+float(row[3])
                    pr_mesic_max[4]=pr_mesic_max[4]+float(row[4])
                    pr_mesic_min[4]=pr_mesic_min[4]+float(row[5])
            if int(row[1])==6:
                    pr_mesic_list[5]=pr_mesic_list[5]+float(row[3])
                    pr_mesic_max[5]=pr_mesic_max[5]+float(row[4])
                    pr_mesic_min[5]=pr_mesic_min[5]+float(row[5])
            if int(row[1])==7:
                    pr_mesic_list[6]=pr_mesic_list[6]+float(row[3])
                    pr_mesic_max[6]=pr_mesic_max[6]+float(row[4])
                    pr_mesic_min[6]=pr_mesic_min[6]+float(row[5])
            if int(row[1])==8:
                    pr_mesic_list[7]=pr_mesic_list[7]+float(row[3])
                    pr_mesic_max[7]=pr_mesic_max[7]+float(row[4])
                    pr_mesic_min[7]=pr_mesic_min[7]+float(row[5])
            if int(row[1])==9:
                    pr_mesic_list[8]=pr_mesic_list[8]+float(row[3])
                    pr_mesic_max[8]=pr_mesic_max[8]+float(row[4])
                    pr_mesic_min[8]=pr_mesic_min[8]+float(row[5])
            if int(row[1])==10:
                    pr_mesic_list[9]=pr_mesic_list[9]+float(row[3])
                    pr_mesic_max[9]=pr_mesic_max[9]+float(row[4])
                    pr_mesic_min[9]=pr_mesic_min[9]+float(row[5])
            if int(row[1])==11:
                    pr_mesic_list[10]=pr_mesic_list[10]+float(row[3])
                    pr_mesic_max[10]=pr_mesic_max[0]+float(row[4])
                    pr_mesic_min[10]=pr_mesic_min[10]+float(row[5])
            if int(row[1])==12:
                    pr_mesic_list[11]=pr_mesic_list[11]+float(row[3])
                    pr_mesic_max[11]=pr_mesic_max[11]+float(row[4])
                    pr_mesic_min[11]=pr_mesic_min[11]+float(row[5])
                    
            if int(row[0])-int(remember)==1:
                if(int(remember)%4!=0):
                    prumer_list.append(round(summa_tmp/365, 3))
                    prumer_max.append(round(summa_max/365, 3))
                    prumer_min.append(round(summa_min/365, 3))
                    rok.append(int(remember))
                elif(int(remember)%4==0):
                    prumer_list.append(round(summa_tmp/366, 3))
                    prumer_max.append(round(summa_max/366, 3))
                    prumer_min.append(round(summa_min/366, 3))
                    rok.append(int(remember))
                summa_tmp=0
                summa_max=0
                summa_min=0
                remember=0                    
            if int(row[0])%4!=0:
                summa_tmp=(summa_tmp+float(row[3]))
                summa_max=(summa_max+float(row[4]))
                summa_min=(summa_min+float(row[5]))
                remember=row[0]
                continue
    
            if int(row[0])%4==0:
                summa_tmp=(summa_tmp+float(row[3]))
                summa_max=(summa_max+float(row[4]))
                summa_min=(summa_min+float(row[5]))
                remember=row[0]                         
                continue        
           
    plt.figure(1)   
    plt.suptitle('Roční průměrné, minimální a maximální teploty', fontsize=15)
    plt.subplot(2,2,1)
    plt.plot(rok, prumer_list, label='Roční průměrné', color='grey')
    plt.legend()
    plt.xlabel('rok')
    plt.ylabel('teplota')
    plt.subplot(2,2,2)
    plt.plot(rok, prumer_max, label='Maximální teploty', color='darkorange')
    plt.legend()
    plt.xlabel('rok')
    plt.ylabel('min. teplota')
    plt.subplot(2,2,3)
    plt.plot(rok, prumer_min, label='Minimální teploty', color='b')
    plt.legend()
    plt.xlabel('rok')
    plt.ylabel('max. teplota')
    plt.savefig('graf1.pdf')
    
    pr_mesic_list[0]=pr_mesic_list[0]/(31*244)
    pr_mesic_list[1]=pr_mesic_list[1]/((61*29)+(183*28))
    pr_mesic_list[2]=pr_mesic_list[2]/(31*244)
    pr_mesic_list[3]=pr_mesic_list[3]/(30*244)
    pr_mesic_list[4]=pr_mesic_list[4]/(31*244)
    pr_mesic_list[5]=pr_mesic_list[5]/(30*244)
    pr_mesic_list[6]=pr_mesic_list[6]/(31*244)
    pr_mesic_list[7]=pr_mesic_list[7]/(31*244)
    pr_mesic_list[8]=pr_mesic_list[8]/(30*244)
    pr_mesic_list[9]=pr_mesic_list[9]/(31*244)
    pr_mesic_list[10]=pr_mesic_list[10]/(30*244)
    pr_mesic_list[11]=pr_mesic_list[11]/(31*244)
    
    pr_mesic_max[0]=pr_mesic_max[0]/(31*244)
    pr_mesic_max[1]=pr_mesic_max[1]/((61*29)+(183*28))
    pr_mesic_max[2]=pr_mesic_max[2]/(31*244)
    pr_mesic_max[3]=pr_mesic_max[3]/(30*244)
    pr_mesic_max[4]=pr_mesic_max[4]/(31*244)
    pr_mesic_max[5]=pr_mesic_max[5]/(30*244)
    pr_mesic_max[6]=pr_mesic_max[6]/(31*244)
    pr_mesic_max[7]=pr_mesic_max[7]/(31*244)
    pr_mesic_max[8]=pr_mesic_max[8]/(30*244)
    pr_mesic_max[9]=pr_mesic_max[9]/(31*244)
    pr_mesic_max[10]=pr_mesic_max[10]/(30*244)
    pr_mesic_max[11]=pr_mesic_max[11]/(31*244)

    pr_mesic_min[0]=pr_mesic_min[0]/(31*244)
    pr_mesic_min[1]=pr_mesic_min[1]/((61*29)+(183*28))
    pr_mesic_min[2]=pr_mesic_min[2]/(31*244)
    pr_mesic_min[3]=pr_mesic_min[3]/(30*244)
    pr_mesic_min[4]=pr_mesic_min[4]/(31*244)
    pr_mesic_min[5]=pr_mesic_min[5]/(30*244)
    pr_mesic_min[6]=pr_mesic_min[6]/(31*244)
    pr_mesic_min[7]=pr_mesic_min[7]/(31*244)
    pr_mesic_min[8]=pr_mesic_min[8]/(30*244)
    pr_mesic_min[9]=pr_mesic_min[9]/(31*244)
    pr_mesic_min[10]=pr_mesic_min[10]/(30*244)
    pr_mesic_min[11]=pr_mesic_min[11]/(31*244)

    plt.figure(2)
    plt.suptitle('Měsíční průměrně, minimální a maximální teploty', fontsize=15)
    plt.plot(mesic, pr_mesic_list, color='gold', label='Měsíční průměrně teploty')
    plt.legend()
    plt.plot(mesic, pr_mesic_max, color='darkorange', linestyle='-.', linewidth=3, label='Měsíční maximální teploty')
    plt.legend()
    plt.plot(mesic, pr_mesic_min, color='skyblue', linestyle='--', linewidth=3, label='Měsíční minimální teploty')
    plt.legend()
    plt.xlabel('měsíc')
    plt.ylabel('teploty')
    plt.savefig('graf2.pdf')
    

    
