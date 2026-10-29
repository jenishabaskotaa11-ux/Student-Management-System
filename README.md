# Student Management System

This is a beginner Python project I built to practice programming fundamentals and file handling. It is a simple, menu-driven application that allows users to manage student records and save their data using JSON.

## Features

- **Add students:** Add a student's name, age, and marks.
- **Search students:** Find student records by name.
- **Update marks:** Change a student's marks with input validation.
- **Delete students:** Remove a student record.
- **View all students:** Display all saved student records.
- **Input validation:** Check age and marks to reduce invalid inputs.
- **JSON storage:** Save student records in a JSON file.
- **Data persistence:** Keep records saved even after closing and restarting the program.
- **Unique student IDs:** Give each record a unique ID while allowing different students to have the same name.

## Technologies Used

- Python 3
- JSON
- File handling
- Dictionaries and nested dictionaries
- Loops and conditional statements
- Input validation

## How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

   ```bash
   python mainfile.py
   ```

   On Windows, you can also try:

   ```bash
   py mainfile.py
   ```

5. Follow the instructions displayed in the terminal to manage student records.

## Data Storage

The program stores student records in `std_system.json`. When the program starts, it loads existing records from the file. Changes made when adding, updating, or deleting students are saved so they remain available the next time the program runs.

If the JSON file does not exist, the program creates it with the initial sample records.

## What I Learned

Building this project helped me practice:

- Working with dictionaries and nested data.
- Using loops and conditional statements to control program flow.
- Validating user input.
- Reading and writing JSON files.
- Implementing basic Create, Read, Update, and Delete (CRUD) operations.
- Saving and loading data between program runs.
- Using Git and GitHub to manage and publish my code.

## Future Improvements

- Allow users to select a specific student by ID when multiple students share the same name.
- Improve error handling for missing or corrupted data files.
- Integrate a database such as SQL Server.
- Add a graphical user interface.

---

**Project type:** Beginner Python project  
**Status:** Working prototype
