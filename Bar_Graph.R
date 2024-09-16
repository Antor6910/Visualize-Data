#laod necessary library
library(ggplot2)

#Read the data from the file
data<- data.frame(
  Category=c("A","B","C","D"),
  Value=c(10,20,30,40)
)



#Basic Bar Graph
ggplot(data,aes(x=Category,y=Value))+
  geom_bar(stat="identity")+
  theme_minimal()+
  labs(title = "Basic Bar Graph",x="Category",y="Value")