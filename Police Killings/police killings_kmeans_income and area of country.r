
library(ggplot2)
#read the data
data=read.csv("clean_police_killings.csv")
head(data)
#set seed for reproducibility
set.seed(20)
#cluster data
cluster = kmeans(data[19], 4, nstart = 20)
cluster
table(cluster$cluster, data$Areaofcountry)
cluster$cluster = as.factor(cluster$cluster)
ggplot(data,aes(ID,householdmedianincome, color=cluster$cluster)) + geom_point()
