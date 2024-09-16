#load necessary library
library(ggplot2)

#download and read data from a url
url<-"https://example.com/data.data.csv"
data<- read.csv(url)

#Create a basic bar graph
ggplot(data,aes(x=Category,y=Value))+
  geom_bar(stat = "identity")+
  theme_minimal()+
  labs(title = "Basic Bar Graph",x="Category",y="Value")