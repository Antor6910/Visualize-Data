import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#----------Problem 1: Genome-Wide Association Studies(GWAS)-------#
#This ensures that the random numbers generated are the same every time the code is run.
np.random.seed(42)

#Define the number of customers to generate data for.
num_customer=300

#Generate purchase frequencies for customers using a Poisson distribution.
#This simulates how many purchase each customers makes on average.
#This mean of the poisson distribution is set to 10.
purchase_frequency=np.random.poisson(10,num_customer) #Purchase frequency

#Calculate the total spend for each customer.
#Multiply their purchase frequency by a random spending amount(between 50 and 500)
#This simulates variability in how much customers spend per purchase.
total_spend=purchase_frequency*np.random.uniform(50,500,num_customer) #Total spend

#Calculate the Customers Lifetime Value(CLV) for each customer.
#Multiply their total spend by a random factor(between 0.8 and 1.2)
#This introduces variability in how much value a customer contributes over time.
clv=total_spend*np.random.uniform(0.8,1.2,num_customer) #Customer Lifetime Value(clv)


#combine into a DataFrame
customer_data=pd.DataFrame({
    "Purchase Frequency":purchase_frequency,
    "Total Spend":total_spend,
    "Customer Lietime Value":clv
})

#Scatter plot for Purchase Frequency vs Total Spend
plt.figure(figsize=(10,6))
plt.scatter(customer_data["Purchase Frequency"], customer_data["Total Spend"], alpha=0.7, color="blue")
plt.title("Customer Behavior: Purchase Frequency vs Total Spend")
plt.xlabel("Purchase Frequency")
plt.ylabel("Total Spend")
plt.grid(True)
plt.tight_layout()
plt.show()