import csv
import os

# ─────────────────────────────────────────
#  Employee Class
# ─────────────────────────────────────────
class Employee:
    def __init__(self, emp_id, name, department, designation, salary):
        self.emp_id      = emp_id
        self.name        = name
        self.department  = department
        self.designation = designation
        self.salary      = float(salary)

    def display(self):
        print(f"{self.emp_id:<8} {self.name:<15} {self.department:<12} "
              f"{self.designation:<15} {self.salary:<10.2f}")


# ─────────────────────────────────────────
#  Global employee list
# ─────────────────────────────────────────
employees = []
# ─────────────────────────────────────────
#  Helper: print table header
# ────────────────────────────────────────
def print_header():
    print("-" * 68)
    print(f"{'ID':<8} {'Name':<15} {'Department':<12} {'Designation':<15} {'Salary':<10}")
    print("-" * 68)


# ─────────────────────────────────────────
#  Part B: Add Employee
# ─────────────────────────────────────────
def add_employee():
    print("\n--- Add Employee ---")
    emp_id = input("Enter Employee ID   : ").strip()

    # Duplicate ID check
    for e in employees:
        if e.emp_id == emp_id:
            print("⚠  Employee with this ID already exists.")
            return

    name        = input("Enter Name          : ").strip()
    department  = input("Enter Department    : ").strip()
    designation = input("Enter Designation   : ").strip()

    while True:
        try:
            salary = float(input("Enter Salary        : ").strip())
            break
        except ValueError:
            print("   Invalid salary. Please enter a number.")

    emp = Employee(emp_id, name, department, designation, salary)
    employees.append(emp)
    print("✔  Employee added successfully!")


# ─────────────────────────────────────────
#  Part C: View Employees
# ─────────────────────────────────────────
def view_employees():
    print("\n--- All Employees ---")
    if not employees:
        print("No employee records found.")
        return
    print_header()
    for e in employees:
        e.display()
    print("-" * 68)


# ─────────────────────────────────────────
#  Part D: Search Employee
# ─────────────────────────────────────────
def search_employee():
    print("\n--- Search Employee ---")
    print("1. Search by ID")
    print("2. Search by Name")
    choice = input("Choose option: ").strip()

    found = []
    if choice == "1":
        emp_id = input("Enter Employee ID: ").strip()
        found  = [e for e in employees if e.emp_id == emp_id]
    elif choice == "2":
        name  = input("Enter Employee Name: ").strip().lower()
        found = [e for e in employees if e.name.lower() == name]
    else:
        print("Invalid option.")
        return

    if found:
        print_header()
        for e in found:
            e.display()
        print("-" * 68)
    else:
        print("Employee Not Found.")


# ─────────────────────────────────────────
#  Part E: Update Employee
# ─────────────────────────────────────────
def update_employee():
    print("\n--- Update Employee ---")
    emp_id = input("Enter Employee ID to update: ").strip()

    for e in employees:
        if e.emp_id == emp_id:
            print(f"Updating record for: {e.name}")
            dept = input(f"New Department  [{e.department}]  : ").strip()
            desig = input(f"New Designation [{e.designation}]: ").strip()
            sal   = input(f"New Salary      [{e.salary}]    : ").strip()

            if dept:
                e.department  = dept
            if desig:
                e.designation = desig
            if sal:
                try:
                    e.salary = float(sal)
                except ValueError:
                    print("   Invalid salary. Salary not updated.")

            print("✔  Employee updated successfully!")
            return

    print("Employee Not Found.")


# ─────────────────────────────────────────
#  Part F: Delete Employee
# ─────────────────────────────────────────
def delete_employee():
    print("\n--- Delete Employee ---")
    emp_id = input("Enter Employee ID to delete: ").strip()

    for i, e in enumerate(employees):
        if e.emp_id == emp_id:
            employees.pop(i)
            print("✔  Employee Deleted Successfully.")
            return

    print("Employee Not Found.")


# ─────────────────────────────────────────
#  Part G: Salary Statistics
# ─────────────────────────────────────────
def salary_statistics():
    print("\n--- Salary Statistics ---")
    if not employees:
        print("No employee records found.")
        return

    salaries = [e.salary for e in employees]
    print(f"  Total Employees : {len(employees)}")
    print(f"  Highest Salary  : {max(salaries):.2f}")
    print(f"  Lowest Salary   : {min(salaries):.2f}")
    print(f"  Average Salary  : {sum(salaries)/len(salaries):.2f}")


# ─────────────────────────────────────────
#  Part H: Export Data
# ─────────────────────────────────────────
def export_data():
    print("\n--- Export Data ---")
    if not employees:
        print("No records to export.")
        return

    filename = "employees.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Designation", "Salary"])
        for e in employees:
            writer.writerow([e.emp_id, e.name, e.department, e.designation, e.salary])

    print(f"✔  Data exported to '{filename}' successfully!")

    # Read back and display
    print("\n--- Records from CSV ---")
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("  ", " | ".join(row))


# ─────────────────────────────────────────
#  Bonus: Department-wise Count
# ─────────────────────────────────────────
def dept_wise_count():
    print("\n--- Department-wise Employee Count ---")
    if not employees:
        print("No records found.")
        return

    dept_count = {}
    for e in employees:
        dept_count[e.department] = dept_count.get(e.department, 0) + 1

    print(f"  {'Department':<20} {'Count'}")
    print("  " + "-" * 28)
    for dept, count in sorted(dept_count.items()):
        print(f"  {dept:<20} {count}")


# ─────────────────────────────────────────
#  Bonus: Sort Employees by Salary
# ─────────────────────────────────────────
def sort_by_salary():
    print("\n--- Employees Sorted by Salary ---")
    if not employees:
        print("No records found.")
        return

    sorted_emps = sorted(employees, key=lambda e: e.salary, reverse=True)
    print_header()
    for e in sorted_emps:
        e.display()
    print("-" * 68)


# ─────────────────────────────────────────
#  Main Menu
# ─────────────────────────────────────────
def main():
    while True:
        print("\n" + "=" * 40)
        print("   EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 40)
        print("  1. Add Employee")
        print("  2. View All Employees")
        print("  3. Search Employee")
        print("  4. Update Employee")
        print("  5. Delete Employee")
        print("  6. Salary Statistics")
        print("  7. Export Data (CSV)")
        print("  8. Department-wise Count ")
        print("  9. Sort by Salary        ")
        print("  0. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if   choice == "1": add_employee()
        elif choice == "2": view_employees()
        elif choice == "3": search_employee()
        elif choice == "4": update_employee()
        elif choice == "5": delete_employee()
        elif choice == "6": salary_statistics()
        elif choice == "7": export_data()
        elif choice == "8": dept_wise_count()
        elif choice == "9": sort_by_salary()
        elif choice == "0":
            print("Exiting.....")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()