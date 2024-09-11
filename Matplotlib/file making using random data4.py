import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Random Student Result Data and Save to Excel
def generate_and_save_student_data(filename, num_students=10):
    """
    Generates random student result data and saves it to an Excel file.

    :param filename: The name of the Excel file to save data.
    :param num_students: The number of students to generate data for.
    """
    # Generate random data
    np.random.seed(0)  # For reproducibility
    data = {
        'Student Name': [f"Student {i+1}" for i in range(num_students)],
        'Math': np.random.randint(40, 100, size=num_students),
        'Science': np.random.randint(35, 95, size=num_students),
        'English': np.random.randint(30, 90, size=num_students),
        'History': np.random.randint(45, 100, size=num_students)
    }

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

# Step 2: Read Data from Excel File using pandas
def read_student_data(filename):
    """
    Reads student result data from an Excel file using pandas.

    :param filename: The name of the Excel file to read data from.
    :return: DataFrame with student results.
    """
    df = pd.read_excel(filename)
    return df

# Step 3: Visualize Data using Bar Chart and Pie Chart
def visualize_student_data(df):
    """
    Visualizes student result data using bar chart and pie chart.

    :param df: DataFrame containing student result data.
    """
    # Bar chart of average marks in each subject
    df.set_index('Student Name', inplace=True)  # Set 'Student Name' as index
    average_marks = df.mean().sort_values()

    plt.figure(figsize=(10, 6))
    average_marks.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Average Marks in Each Subject')
    plt.xlabel('Subjects')
    plt.ylabel('Average Marks')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Pie chart of total marks distribution for the first student
    first_student = df.iloc[0]
    plt.figure(figsize=(8, 8))
    plt.pie(first_student, labels=first_student.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(f"Marks Distribution for {first_student.name}")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# Main Execution
if __name__ == '__main__':
    filename = 'student_results.xlsx'

    # Generate and save random student data to Excel
    generate_and_save_student_data(filename)
    print(f"Student data has been generated and written to {filename}.")

    # Read data from Excel file using pandas
    df = read_student_data(filename)

    # Visualize the student result data
    visualize_student_data(df)
