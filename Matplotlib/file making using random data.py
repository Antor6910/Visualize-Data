import csv
import random
import matplotlib.pyplot as plt
#Step 1:Generating random data
def generate_random_data(filename,num_points=100):

    """
    Generate random data and write it to a csv file.

    :param filename: Name of the file to write data to
    :param num_points: Number of data points to generate
    """
    with open(filename,'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Index","Value"]) #writer header
        for i in range(num_points):
            writer.writerow([i,random.uniform(0,100)]) #Random float between 0 to 100


#step 2:Read data from csv file
def read_data(filename):
    indices,values=[],[]
    with open(filename,'r') as file:
        reader=csv.reader(file)
        next(reader) #skip header
        for row in reader:
            indices.append(int(row[0]))
            values.append(float(row[1]))
    return indices,values


#step 3:Visualization data using matplotlib
def visualize_data(indices,values):
    plt.plot(indices,values,marker='o',linestyle='-',color='g',label='line Plot')
    plt.scatter(indices,values,color='r',label='scatter plot')
    plt.title("Random data visualization.")
    plt.xlabel('Index')
    plt.ylabel('value')
    plt.legend()
    plt.grid(True)
    plt.show()

#Main Execution
if __name__=="__main__":
    filename='random_data.csv'

    generate_random_data(filename) #generate and save data
    indices,values=read_data(filename) #read data from the csv file
    visualize_data(indices, values) #Visialize the data
