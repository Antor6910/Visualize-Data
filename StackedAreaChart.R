library(ggplot2)

ggplot(uspoage,aes(x=Year,y=Thousands,fill=AgeGroup))+
  geom_area()+
  labs(title = "US Population by age",x="Year",y="Population in thousands")