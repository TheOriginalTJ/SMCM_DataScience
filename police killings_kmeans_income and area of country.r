library(datasets)
library(ggplot2)

getwd()
data=read.csv("clean_police_killings.csv")
head(data)
set.seed(20)
cluster = kmeans(data[19], 4, nstart = 20)
cluster
table(cluster$cluster, data$Areaofcountry)
cluster$cluster = as.factor(cluster$cluster)
ggplot(data,aes(ID,householdmedianincome, color=cluster$cluster)) + geom_point()
