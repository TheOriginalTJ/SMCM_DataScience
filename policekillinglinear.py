# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:54:53 2017

@author: JP
Purpose: This code is to generate a linear regression using a police killings data set. The two axis are:
-Personal household income is X axis
-Nonewhite percentage is Y axis

Our hypothesis is that the regression will show a trend of low income households having a higher concentration 
of police killings, as well as an even greater concentration in non-white groups.


We can assume that 
0-39% is non-white
40-79% is "mixed"
80-100% is white

USES police_killings.csv"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model


infile = open('police_killings.csv', 'r')


medianhouseincome = []
percentwhite = []


next(infile)
#Iterates through police_killings.csv by row to choose two columns: % White and Median Household Income
for line in infile:
        row = line.split(",")
        if row[17] == 'NA' or row[14] == 'NA':
            break
        medianhouseincome.append(int(row[17]))
        percentwhite.append((float(row[14])))
        

xo = medianhouseincome
yo = percentwhite

x = np.array(xo).reshape(-1,1)
y = np.array(yo).reshape(-1,1)

x_train = x[:-10]
y_train = y[:-10]

x_test = x[-10:]
y_test = y[-10:]

regr = linear_model.LinearRegression()

regr.fit(x_train, y_train)

print('Coefficients: ' + str(regr.coef_))

pred = regr.predict([10])
print pred

plt.scatter(x, y, color = 'black')
plt.plot(x_test, regr.predict(x_test), color='red', linewidth=1)
plt.ylim([-5,105])
plt.ylabel('% White')
plt.xlabel('Median Household Income')
plt.title('Police Killings Linear Regression: % White vs Median Household Income')
plt.grid(True)

plt.show()


plt.savefig('PoliceKillingsLinear_percentWhiteVShouseholdIncome.png')