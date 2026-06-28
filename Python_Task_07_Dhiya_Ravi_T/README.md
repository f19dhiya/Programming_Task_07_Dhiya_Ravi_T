# Employee Management System

This is my Task 07 project for the White Band Associates Python Internship. In this task I built a simple Employee Management System using Object-Oriented Programming concepts in Python.

---

## What This Project Does

This is a menu-driven command line application where you can manage employee records. You can add employees, view them, search, update, delete, and also export the data to a CSV file.

---

## How to Run

Make sure you have Python installed (Python 3.x).

Then just run:

```
python employee_management.py
```

No extra libraries needed. Everything used here is part of Python's standard library.

---

## Features

- Add a new employee with ID, name, department, designation and salary
- View all employees in a table format
- Search employee by ID or by name
- Update department, designation or salary of any employee
- Delete an employee using their ID
- View salary statistics like highest, lowest and average salary
- Export all records to a CSV file and read them back
- Bonus: See employee count department-wise
- Bonus: Sort all employees by salary

---

## Files in This Folder

| File | Description |
|------|-------------|
| employee_management.py | Main Python program |
| employees.csv | Sample employee data / exported file |
| README.md | This file |

---

## Concepts I Learned

- How to create a Class and use `__init__` constructor
- How to create objects and store them in a list
- How to write methods inside a class
- How to use loops and conditions to build a menu system
- How to read and write CSV files using the `csv` module
- Basic OOP principles like encapsulation

---

## Sample Output

```
========================================
   EMPLOYEE MANAGEMENT SYSTEM
========================================
  1. Add Employee
  2. View All Employees
  3. Search Employee
  4. Update Employee
  5. Delete Employee
  6. Salary Statistics
  7. Export Data (CSV)
  8. Department-wise Count  [Bonus]
  9. Sort by Salary         [Bonus]
  0. Exit
========================================

--------------------------------------------------------------------
ID       Name            Department   Designation     Salary
--------------------------------------------------------------------
101      Soham           IT           Developer       50000.00
102      Rahul           HR           Manager         65000.00
--------------------------------------------------------------------
```

---

## Notes

I kept the code simple and easy to read. Each feature is written as a separate function so it's easy to understand what each part does. I also added some basic validation like checking for duplicate employee IDs and making sure salary input is a number.

This was a really helpful task to understand how real-world applications are structured using classes and objects.
