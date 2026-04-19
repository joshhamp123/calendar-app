import csv   # Allows the program to read and write CSV files
import os    # Allows the program to check if the CSV file exists

FILENAME = "tasks.csv"   # The name of the CSV file where tasks will be stored


# This function creates the CSV file if it does not already exist
def setup_file():
    if not os.path.exists(FILENAME):   # Check if the file is missing
        with open(FILENAME, "w", newline="") as file:   # Create the file in write mode
            writer = csv.writer(file)   # Create a CSV writer object
            writer.writerow(["id", "title", "date"])   # Write the header row

# This function adds a new task to the CSV file
def add_task():
    print("\n--- Add Task ---")
    title = input("Enter task title: ")   # Ask the user for the task title
    date = input("Enter task date (YYYY-MM-DD): ")   # Ask for the task date

    tasks = []   # List to store all tasks temporarily

    # Read all existing tasks so we can find the next ID
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)   # Read the CSV file
        for row in reader:          # Loop through each row
            tasks.append(row)       # Add each row to the list

    # If only the header exists, start IDs at 1
    if len(tasks) <= 1:
        next_id = 1
    else:
        last_id = int(tasks[-1][0])   # Get the last task's ID
        next_id = last_id + 1         # New ID is last ID + 1

    # Write the new task to the CSV file
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([next_id, title, date])   # Add the new task row

    print("Task added!")   # Confirmation message


# This function displays all tasks in the CSV file
def view_tasks():
    print("\n--- All Tasks ---")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)   # Read the CSV file
        for row in reader:          # Loop through each row
            print(row)              # Print the row to the screen


# This function deletes a task using its ID
def delete_task():
    print("\n--- Delete Task ---")
    delete_id = input("Enter the ID of the task to delete: ")   # Ask for ID

    tasks = []   # List to store all tasks

    # Read all tasks from the CSV file
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            tasks.append(row)

    # Write back only the tasks that do NOT match the ID
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for row in tasks:
            if row[0] != delete_id:   # Keep all rows except the one to delete
                writer.writerow(row)

    print("Task deleted (if it existed).")   # Confirmation message


# This is the main menu loop that runs the program
def main():
    setup_file()   # Make sure the CSV file exists before starting

    while True:   # Loop forever until the user chooses to exit
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")   # Ask the user for a menu choice

        if choice == "1":
            add_task()        # Call the add task function
        elif choice == "2":
            view_tasks()      # Call the view tasks function
        elif choice == "3":
            delete_task()     # Call the delete task function
        elif choice == "4":
            print("Goodbye")  # Exit message
            break             # Break the loop to end the program
        else:
            print("Invalid choice")   # Handle wrong input


main()   # Start the program