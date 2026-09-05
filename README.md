# Student Management System with File Storage

**Description:**
This project includes three main files and handles student information:

1. **main.py**  
   The program asks the user to enter the name and grade of 3 students.  
   If the grade is not a valid float number, the program shows an error message and asks the user to re-enter.  
   After collecting all data, each student is stored as a `Student` object and then saved to the file `student.txt`.  
   Finally, the saved data is loaded and displayed.

2. **models/student.py**  
   The `Student` class is defined with two attributes:  
   - `name` (string)  
   - `grade` (floating point)  
   The method `info()` returns a formatted string showing the student’s name and grade.

3. **utils/file_manager.py**  
   Two functions are provided:  
   - `save_students(path, students)`: Saves the list of students to `student.txt`.  
     - If the file exists, data is appended to the end (`open(path, 'a')`).  
     - If the file does not exist, a new file is created (`open(path, 'x')`).  
     - Proper error messages are shown for permission errors or unexpected exceptions.  
   - `load_students(path)`: Reads the file `student.txt`, splits each line into name and grade, and returns a list of `Student` objects.  
     If the file does not exist or a reading error occurs, an empty list is returned.

**Important Note:**  
If the program was run previously and the user had entered invalid data, the program would read and display the old data from the file.  
To avoid this issue, you must delete the `student.txt` file before running the program for the first time. After deletion, the program will start fresh from the beginning.
