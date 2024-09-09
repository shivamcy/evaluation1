
employee_directory = {}
def add_employee(emp_id, name, department, salary):
    if emp_id in employee_directory:
        print(f"Employee  ID  exists.")
    else:
        employee_directory[emp_id] = {
            'Name': name,
            'Department': department,
            'Salary': salary
        }
        print(f"Employee {name} added ")


def upd_employee(emp_id, name=None, department=None, salary=None):
    if emp_id in employee_directory:
        if name is not None:
            employee_directory[emp_id]['Name'] = name
        if department is not None:
            employee_directory[emp_id]['Department'] = department
        if salary is not None:
            employee_directory[emp_id]['Salary'] = salary
        print(f"Employee ID updated successfully.")
    else:
        print(f"Employee with ID  not found.")

def search_employee(emp_id):
    employee = employee_directory.get(emp_id)
    if employee:
        print(f" ID: {emp_id}")
        print(f"Name: {employee['Name']}")
        print(f"Department: {employee['Department']}")
        print(f"Salary: {employee['Salary']}")
    else:
        print(f"Employee not found.")

def dep_report():
    department_dict = {}
    for emp_id, details in employee_directory.items():
        department = details['Department']
        if department not in department_dict:
            department_dict[department] = []
        department_dict[department].append({
            'ID': emp_id,
            'Name': details['Name'],
            'Salary': details['Salary']
        })
    
    for department, employees in department_dict.items():
        print(f"Department: {department}")
        for emp in employees:
            print(f"ID: {emp['ID']}, Name: {emp['Name']}, Salary: {emp['Salary']}")

def main_menu():
    while True:
        
        print("1. Add employee")
        print("2. Update employee")
        print("3. Search employee by ID")
        print("4. Generate  report")
        print("5. Exit program")

        
        choice = input("Enter choice: ")
        
        if choice == '1':
            emp_id = input("Enter  ID: ")
            name = input("Enter  Name: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            add_employee(emp_id, name, department, salary)
        
        elif choice == '2':
            emp_id = input("Enter ID to update: ")
            name = input("Enter new employee name: ")
            department = input("Enter new department : ")
            salary_input = input("Enter new salary : ")
            salary = float(salary_input) if salary_input else None
            upd_employee(emp_id, name if name else None, department if department else None, salary)
        
        elif choice == '3':
            emp_id = input("Enter employee ID: ")
            search_employee(emp_id)
        
        elif choice == '4':
            dep_report()
        elif choice=='5':
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()

