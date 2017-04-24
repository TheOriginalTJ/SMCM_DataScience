# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:19:01 2017

@author: Megan
"""
from matplotlib import pyplot as plt
import numpy as np
from sklearn import linear_model

#read in the data
file1 = "police_killings.csv"
file2 = "poverty_by_state_2015.csv"

f1 = open(file1, "r")

p_income = []
h_income = []
c_income = []
avgc_income = []
white = []
black = []
hispanic = []
state = []
ID_name = list(range(465))

next(f1)
for line in f1:
   row = line.split(",")
   state.append(row[4])
   p_income.append(float(row[11]))
   h_income.append(float(row[12]))
   c_income.append(float(row[14]))
   avgc_income.append(float(row[13]))
   white.append(float(row[8]))
   black.append(float(row[9]))
   hispanic.append(float(row[10]))

#open the file 2 of poverty rates in 2015 by state
f2 = open(file2, "r")

states = []
pov2015 = []

next(f2)
for line in f2:
    row = line.split(",")
    states.append(row[0])
    pov2015.append(float(row[1]))
    
   
#personal income
income = np.array(p_income).reshape(-1, 1)
ID = np.array(ID_name).reshape(-1, 1)
income_train = income[:-200]
ID_train = ID[:-200]
income_test = income
ID_test = ID

regr = linear_model.LinearRegression()
regr.fit(ID_train, income_train)
   
#scatterplot of the data
plt.figure(figsize=(18,15))
plt.title("Average Personal Income of Victims")
plt.xlabel("Number of Victims")
plt.ylabel("Personal Income")
plt.scatter(ID_name, p_income, color = 'black')
plt.plot(ID_test, regr.predict(ID_test), color='red', linewidth=4)
plt.savefig('police_killings_personal_income.png')
plt.show()

#household income
h_income = np.array(h_income).reshape(-1, 1)
h_income_train = h_income[:-200]
h_income_test = h_income
regr.fit(ID_train, h_income_train)
   
#scatterplot of the data
plt.figure(figsize=(18,15))
plt.title("Average Household Income of Victims")
plt.xlabel("Number of Victims")
plt.ylabel("Household Income")
plt.scatter(ID_name, h_income, color = 'black')
plt.plot(ID_test, regr.predict(ID_test), color='red', linewidth=4)
plt.savefig('police_killings_household_income.png')
plt.show()

#household v county income
c_income = np.array(c_income).reshape(-1, 1)
c_income_train = c_income[:-200]
c_income_test = c_income
regr.fit(ID_train, c_income_train)
   
#scatterplot of the data
plt.figure(figsize=(18,15))
plt.title("Household/County Income of Victims")
plt.xlabel("Number of Victims")
plt.ylabel("Household Income Compared to County Income")
plt.scatter(ID_name, c_income, color = 'black')
plt.plot(ID_test, regr.predict(ID_test), color='red', linewidth=4)
plt.savefig('police_killings_householdvcounty_income.png')
plt.show()

#%white vs county income
whiteper = np.array(white).reshape(-1, 1)
whiteper_train = whiteper[:-200]
whiteper_test = whiteper
avgc_income = np.array(avgc_income).reshape(-1, 1)
avgc_income_train = avgc_income[:-200]
avgc_income_test = avgc_income

regr = linear_model.LinearRegression()
regr.fit(whiteper_train, avgc_income_train)
   
#scatterplot of the data
plt.figure(figsize=(18,15))
plt.title("Whiteness of County vs. Average County Income")
plt.xlabel("% of Residents that Identify as White")
plt.ylabel("Average County Income")
plt.scatter(whiteper, avgc_income, color = 'black')
plt.plot(whiteper_test, regr.predict(whiteper_test), color='red', linewidth=4)
plt.savefig('police_killings_whiteness_vs_county_income.png')
plt.show()

#%white vs household/county income
whiteper = np.array(white).reshape(-1, 1)
whiteper_train = whiteper[:-200]
whiteper_test = whiteper

regr = linear_model.LinearRegression()
regr.fit(whiteper_train, c_income_train)
   
#scatterplot of the data
plt.figure(figsize=(18,15))
plt.title("Whiteness of County vs. Average County Income")
plt.xlabel("% of Residents that Identify as White")
plt.ylabel("Average County Income")
plt.scatter(whiteper, c_income, color = 'black')
plt.plot(whiteper_test, regr.predict(whiteper_test), color='red', linewidth=4)
plt.savefig('police_killings_whiteness_vs_householdvcounty_income.png')
plt.show()

