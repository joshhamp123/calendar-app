import csv   # Allows the program to read and write CSV files
import os    # Allows the program to check if the CSV file exists

FILENAME = "tasks.csv"   # The name of the CSV file where tasks will be stored


# This function creates the CSV file if it does not already exist
def setup_file():
    if not os.path.exists(FILENAME):   # Check if the file is missing
        with open(FILENAME, "w", newline="") as file:   # Create the file in write mode
            writer = csv.writer(file)   # Create a CSV writer object
            writer.writerow(["id", "title", "date"])   # Write the header row


