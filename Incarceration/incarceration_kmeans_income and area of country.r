library(datasets)
library(ggplot2)

getwd()
data=read.csv("clean_incarceration and income 2004.csv")
head(data)
set.seed(20)
cluster = kmeans(data[1857], 4, nstart = 20)
cluster
table(cluster$cluster, data$V1057)
cluster$cluster = as.factor(cluster$cluster)
p = ggplot(data,aes(V0001,V1857, color=cluster$cluster)) + geom_point()  
p + scale_y_continuous(breaks=c(seq(10000,200000,by=10000)))+ 
  labs(title="K-Means Clustering of Income Prior to incarceration by State of Residence",
       x ="ID", y = "Income") +
  geom_text(aes(label=data$V1057), size=3) 
