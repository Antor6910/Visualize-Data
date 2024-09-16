library(ggplot2)

ggplot(economics,aes(x=date,y=psavert))+
  geom_area(fill="green",color="black")+
  labs(title = "Personal Saving Rate",x="Date",y="Personal Saving Rate")