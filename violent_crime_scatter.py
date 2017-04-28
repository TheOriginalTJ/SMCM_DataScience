# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:42:56 2017

@author: Megan
"""
from matplotlib import pyplot as plt
import numpy as np
from sklearn import linear_model

#read in the data
file1 = "violent_crime_by_state.csv"

f1 = open(file1, "r")

avgpop = [0] *51
avgcrime = []
avgpov = []
pop2015 = []
pop2014 = []
pop2013 = []
crime2015 = []
crime2014 = []
crime2013 = []
crimepercent2015 = []
pov2015 = []
states = [] * 50

next(f1)
for line in f1:
    row = line.split(",")
    if row[0] != "DC":
        states.append(row[0])
        pop2013.append(int(row[1]))
        pop2014.append(int(row[2]))
        pop2015.append(int(row[3]))
        crime2013.append(int(row[4]))
        crime2014.append(int(row[5]))
        crime2015.append(int(row[6]))
        crimepercent2015.append(float(row[7]) * 100)
        avgcrime.append(float(row[8]) * 100)
        avgpov.append(float(row[9]))
        pov2015.append(float(row[10]) * 100)   

for i in range (0, 50):
    avgpop[i] = pop2013[i] + pop2014[i] + pop2015[i]
    avgpop[i] = avgpop[i] / 3

#Scatterplot of average crime

poverty = np.array(avgpov).reshape(-1, 1)
crime = np.array(avgcrime).reshape(-1, 1)
poverty_train = poverty[:-20]
crime_train = crime[:-20]
poverty_test = poverty
crime_test = crime

regr = linear_model.LinearRegression()
regr.fit(crime_train, poverty_train)
   
#scatterplot of the data
plt.figure(figsize=(18,15))
plt.title("States Poverty Rates vs. Violent Crime")
plt.xlabel("Percent of Population Affected by Violent Crime")
plt.ylabel("Percent of Population Under Poverty Level")
plt.scatter(crime, poverty, color = 'black')
plt.plot(crime_test, regr.predict(crime_test), color='red', linewidth=4)
for label, crim, pov in zip(states, crime, poverty):
    plt.annotate(label, xy = (crim, pov), xytext = (5, -5), textcoords = 'offset points')
plt.savefig('violentcrime_avg.png')
plt.show()

   
#Scatterplot of 2015 data only
poverty2015 = np.array(pov2015).reshape(-1, 1)
crimes2015 = np.array(crimepercent2015).reshape(-1, 1)
poverty_train2015 = poverty2015[:-20]
crime_train2015 = crimes2015[:-20]
poverty_test2015 = poverty2015
crime_test2015 = crimes2015

regr = linear_model.LinearRegression()
regr.fit(crime_train2015, poverty_train2015)
   
#scatterplot of the data
plt.figure(figsize=(18,15))
plt.title("States Poverty Rates vs. Violent Crime in 2015")
plt.xlabel("Percent of Population Affected by Violent Crime")
plt.ylabel("Percent of Population Under Poverty Level")
plt.scatter(crimes2015, pov2015, color = 'black')
plt.plot(crime_test, regr.predict(crime_test), color='red', linewidth=4)
for label, crim, pov in zip(states, crimes2015, poverty2015):
    plt.annotate(label, xy = (crim, pov), xytext = (5, -5), textcoords = 'offset points')
plt.savefig('violentcrime_2015.png')
plt.show()
    
    
    
    
    