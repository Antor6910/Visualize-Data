import csv
import random
import matplotlib.pyplot as plt


# Step 1: Generate Random Data and Write to CSV
def generate_and_save_data_for_bar(filename, num_points=10):
    """
    Generates random integer data and saves it to a CSV file.

    :param filename: The name of the CSV file to save data.
    :param num_points: The number of data points to generate.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Value"])  # Write header
        for i in range(num_points):
            category = f"Category {i + 1}"  # Generate category names
            value = random.randint(1, 100)  # Generate random integer values
            writer.writerow([category, value])


# Step 2: Read Data from CSV File
def read_data_for_bar(filename):
    """
    Reads data from a CSV file and returns categories and their corresponding values.

    :param filename: The name of the CSV file to read data from.
    :return: Lists of categories and values.
    """
    categories, values = [], []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            categories.append(row[0])
            values.append(int(row[1]))
    return categories, values


# Step 3: Visualize Data using a Bar Graph in Matplotlib
def visualize_bar_graph(categories, values):
    """
    Visualizes the data using a bar graph.

    :param categories: List of categories (x-axis).
    :param values: List of values (y-axis).
    """
    plt.bar(categories, values, color='skyblue', edgecolor='black')
    plt.title('Bar Graph of Random Data')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Main Execution
if __name__ == '__main__':
    filename = 'bar_graph_data.csv'

    # Generate and save random data to file
    generate_and_save_data_for_bar(filename)
    print(f"Data has been generated and written to {filename}.")

    # Read data from file
    categories, values = read_data_for_bar(filename)

    # Visualize the data using a bar graph
    visualize_bar_graph(categories, values)
