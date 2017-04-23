# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:54:53 2017

@author: JP
"""
"""

Personal household income is X axis
Nonewhite percentage is Y axis

USES police_killings.csv"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model


infile = open('police_killings.csv', 'r')

"Evaluating percent non-white with household income"



medianhouseincome = []
percentwhite = []


next(infile)

for line in infile:
        row = line.split(",")
        if row[17] == 'NA' or row[14] == 'NA':
            break
        medianhouseincome.append(int(row[17]))
        percentwhite.append(100-(float(row[14])))
        
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
plt.show()
print "Y axis is percent non-white (0 = white, 100 = nonwhite)"
print "X axis is median household income"
        