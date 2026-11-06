[README.md](https://github.com/user-attachments/files/34491081/README.md)
# University Information System

A simple command-line program in Python for managing university subjects and students. It reads and saves data in a JSON file and shows which students passed a subject.

## Features

1. Display all subjects with their professor and requirements
2. Display all students
3. Add a new student with their attendance and exam scores
4. Show which students passed a specific subject

A student passes a subject when their attendance and exam score meet the subject's minimum requirements.

The program checks user input and shows a clear message if something is wrong, for example a non-numeric ID or a missing data file.

## How to run

You need Python 3. No extra libraries are required.

```bash
git clone https://github.com/snko7/University-Information-System.git
cd University-Information-System
python main.py
```

## Files

- `main.py`: the program
- `database/database.json`: subjects, professors and students
- `documentation.docx`: project documentation

## Author

Abdulrahman Alsafadi
