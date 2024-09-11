import pandas as pd
import random
import matplotlib.pyplot as plt

# Step 1: Generate Random Data and Write to CSV
def generate_and_save_data_for_bar(filename, num_points=10):
    """
    Generates random integer data and saves it to a CSV file.

    :param filename: The name of the CSV file to save data.
    :param num_points: The number of data points to generate.
    """
    data = {'Category': [f"Category {i+1}" for i in range(num_points)],
            'Value': [random.randint(1, 100) for _ in range(num_points)]}
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Step 2: Read Data from CSV File using pandas
def read_data_for_bar(filename):
    """
    Reads data from a CSV file using pandas and returns categories and their corresponding values.

    :param filename: The name of the CSV file to read data from.
    :return: DataFrame with categories and values.
    """
    df = pd.read_csv(filename)
    return df

# Step 3: Visualize Data using a Bar Graph in Matplotlib
def visualize_bar_graph(df):
    """
    Visualizes the data using a bar graph.

    :param df: DataFrame containing categories and values.

    """
    fig=plt.figure("Data visualization")
    plt.bar(df['Category'], df['Value'], color='skyblue', edgecolor='black')
    plt.title('Bar Graph of Random Data')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main Execution
if __name__ == '__main__':
    filename = 'bar_graph_data1.csv'

    # Generate and save random data to file
    generate_and_save_data_for_bar(filename)
    print(f"Data has been generated and written to {filename}.")

    # Read data from file using pandas
    df = read_data_for_bar(filename)

    # Visualize the data using a bar graph
    visualize_bar_graph(df)
