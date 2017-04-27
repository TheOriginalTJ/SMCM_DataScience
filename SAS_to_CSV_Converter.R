#SAS to CSV Data-File-Converter
#CS480 Data Science with Prof Alan Jamieson at SMCM

library('foreign')
#This is the directory that we want to work in on the local machine. Replace with your target directory on your local machine in this format.
#setwd("C://Users//tjsta//College//St Marys//COSC480 - Data Science//Jail Data from Govt//ICPSR_04572//DS0002")
setwd("C://Users//tjsta//College//St Marys//COSC480 - Data Science//Jail Data from Govt//NSDUH-2015-DS0001-data")

#This process will read in the sas data and then write it out in a usable csv format.
#data = read.xport("04572-0002-Data.xpt")
datanow = read.spss("NSDUH-2015-DS0001-data-spss.sav")
write.csv(datanow, file="LegibleData.csv")
