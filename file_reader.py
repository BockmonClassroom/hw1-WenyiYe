# Name: Wenyi Ye
# Date: Jan.21.2025

import csv

def read_and_print_iris_data(file_path):
    try:
        # Open the file in read mode
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            # Iterate each line in the CSV file
            for line in reader:
                # Print the line
                print(line)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    # Define the file name
    file_name = "data/Iris.csv"
    
    # Call the function
    read_and_print_iris_data(file_name)
