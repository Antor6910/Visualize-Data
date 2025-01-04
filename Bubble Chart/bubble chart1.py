#Question Analysis the performance of different software versions by comparing memory usage,execution time,and the number of users.
import matplotlib.pyplot as plt

#Data for software performance
memory_usage=[500,700,800,600] #X axis:Memory usage in MB
execution_time=[20,50,40,30] #Y axis:Execution time in miliseconds
num_users=[1000,5000,3000,2000] #Bubble Size:Number of users
versions=['v1.0','v2.0','v3.0','v4.0',]

#Bubble Chart
plt.figure(figsize=(10,6))
scatter=plt.scatter(memory_usage,execution_time,s=[n/10 for n in num_users],c=range(len(versions)),cmap='viridis',alpha=0.6,edgecolors='w')
plt.colorbar(scatter,label='Software Version')
plt.xlabel('Memory Usage (MB)')
plt.ylabel('Execution Time (ms)')
plt.title('Software Performance Analysis')
plt.show()
