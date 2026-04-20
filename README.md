 ____        _   _                 
|  _ \ _   _| |_| |__   ___  _ __  
| |_) | | | | __| '_ \ / _ \| '_ \ 
|  __/| |_| | |_| | | | (_) | | | |
|_|    \__, |\__|_| |_|\___/|_| |_|
       |___/      TASK MANAGER CLI


This is a command-line Task Manager application written in Python. 
It allows the user to add tasks, view all saved tasks, and delete tasks using a unique task ID. 
All task data is stored permanently in a CSV file called tasks.csv, allowing the program to be closed and reopened without losing information.

Key Features:

• Add a new task (title, date, time)
• View all saved tasks
• Delete a task using its ID
• Automatic CSV file creation
• Input validation for date and time formats
• Error handling for invalid user input
• Menu-driven interface

How to run/ use the program?

1. Make sure Python 3 is installed.
2. Open a terminal inside the project folder.
3. Run the program using:   python main.py

File structure:

calendar-app/
│
├── main.py          # Main program file
├── tasks.csv        # CSV file where tasks are stored
├── README.txt       # Instructions for running the program
└── .git             # Exported Git commit history

Association with the csv file and its usage:

The program stores all tasks in tasks.csv.
If the file does not exist, the program automatically creates it with the header:

id,title,date,time

Each new task is assigned a unique ID and appended to the file.

Methodology 

This project was developed using an Agile/Kanban approach. 
Tasks were organised into a Kanban board with columns such as:
• To Do
• In Progress
• Testing
• Completed

This helped break the project into small, manageable tasks and track progress clearly.

Use of AI:

AI tools were used to support development by:
• Generating example code structures
• Providing suggestions and explanations of Python functions
• Helping debug errors
• Assisting with methodolgy choice and creation of a repository 

All AI-generated code was reviewed, tested, and adapted to ensure understanding.

version control (git and GitHub )

Version control was managed using Git and GitHub.
Feature-based commits were used to track progress, including:
• Initial project setup
• Adding CSV file handling
• Implementing add/view/delete functions
• Input validation improvements
• Final testing and cleanup

A full git log is included in a .git folder 

future improvements/ suggestions 

• Add task editing functionality
• Add colour-coded priority levels
• Add search/filter options
• Convert to a GUI application






