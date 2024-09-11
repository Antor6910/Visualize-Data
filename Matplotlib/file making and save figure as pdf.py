import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Generate  a sample data

data={
    'Student Name':['Student 1','Student 2','Student 3','Student 4','Student 5'],
    'Math':[88,92,79,85,90],
    'Science':[84,95,76,91,89],
    'English':[78,83,88,35,82],
    'History':[90,85,82,87,93]
}

#Create a DataFrame
df=pd.DataFrame(data)
df.set_index('Student Name',inplace=True)

#plot bar chart of average marks in each subject
average_marks=df.mean().sort_values()
plt.figure(figsize=(10,6))
average_marks.plot(kind='bar',color='skyblue',edgecolor='black',)
plt.title('Average Marks in Each subject')
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.xticks(rotation=45)
plt.tight_layout()

#stop to save the plot as a pdf file
plt.savefig('student_average_marks.pdf')  #Save as a pdf
plt.show()