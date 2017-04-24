# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:26:20 2017

@author: Caroline M Goyco
"""

import matplotlib.pyplot as plt
import numpy as np

#read in the data
file1 = "clean_incarceration and income 2004.csv"

f1 = open(file1, "r")

ID = []
income = []

group0=0
group1=0
group2=0
group3=0
group4=0
group5=0
group6=0
group7=0
group8=0
group9=0
group10=0
group11=0
group12=0
group13=0
group14=0
group15=0

next(f1)
for line in f1:
    row = line.split(",") 
    ID.append(int(row[0]))
    if(row[1857] == "0"):
        group0+=1
        income.append(0)
    elif(row[1857] == "1"):
        group1+=1
        income.append(199)
    elif(row[1857] == "2"):
        group2+=1
        income.append(399)
    elif(row[1857] == "3"):
        group3+=1
        income.append(599)
    elif(row[1857] == "4"):
        group4+=1
        income.append(799)
    elif(row[1857] == "5"):
        group5+=1
        income.append(999)
    elif(row[1857] == "6"):
        group6+=1
        income.append(1199)   
    elif(row[1857] == "7"):
        group7+=1
        income.append(1499)
    elif(row[1857] == "8"):
        group8+=1
        income.append(1999)
    elif(row[1857] == "9"):
        group9+=1
        income.append(2499)
    elif(row[1857] == "10"):
        group10+=1
        income.append(4999)
    elif(row[1857] == "11"):
        group11+=1
        income.append(7499)
    elif(row[1857] == "12"):
        group12+=1
        income.append(7500)        
    elif(row[1857] == "97"):
        group13+=1
        income.append(-1)
    elif(row[1857] == "98"):
        group14+=1
        income.append(-1)
    elif(row[1857] == "99"):
        group15+=1
        income.append(-1)   
        
y = [group0, group1, group2,group3,group4,
               group5,group6, group7,group8,
               group9,group10, group11, group12,
               group13,group14,group15]
               #parameters for barcharts
interval = ("no income", "1-199", "200-399", "400-599",
            "600-799", "800-999", "1000-1199", "1200-1499",
            "1500-1999", "2000-2499", "2500-4999", "5000-7499",
            "7500+", "Don't know", "Refused", "Blank")
y_pos = np.arange(len(interval))
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(y_pos, y, width, color="blue")
plt.xticks(y_pos, interval,rotation=45)
plt.ylabel('Number of responses')
plt.xlabel('Income range')
plt.title("Reported Monthly Income 1 Month Before Incarceration in 2004")
plt.show()