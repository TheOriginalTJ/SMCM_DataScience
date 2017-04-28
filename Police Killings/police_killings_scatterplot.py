# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:56:26 2017

@author: Caroline M Goyco
"""

import matplotlib.pyplot as plt

#read in the data
file1 = "clean_police_killings.csv"

f1 = open(file1, "r")

p_income = []
ID_name = list(range(467))

next(f1)
for line in f1:
    row = line.split(",") 
    print(row[16])
    p_income.append(int(row[16]))

#scatterplot of the data
plt.scatter(ID_name, p_income, color = 'black')
plt.show()
