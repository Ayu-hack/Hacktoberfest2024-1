#Employee Management System

class Employee:  
    def __init__(self, emp_id, name, position, department, salary):  
        self.emp_id = emp_id  
        self.name = name  
        self.position = position  
        self.department = department  
        self.salary = salary  

    def __str__(self):  
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Department: {self.department}, Salary: {self.salary}"  


class EmployeeManagementSystem:  
    def __init__(self):  
        self.employees = []  

    def add_employee(self, emp_id, name, position, department, salary):  
        new_employee = Employee(emp_id, name, position, department, salary)  
        self.employees.append(new_employee)  
        print(f"Employee {name} added successfully.")  

    def view_employees(self):  
        for employee in self.employees:  
            print(employee)  

    def update_employee(self, emp_id, name=None, position=None, department=None, salary=None):  
        for employee in self.employees:  
            if employee.emp_id == emp_id:  
                if name:  
                    employee.name = name  
                if position:  
                    employee.position = position  
                if department:  
                    employee.department = department  
                if salary:  
                    employee.salary = salary  
                print(f"Employee ID {emp_id} updated successfully.")  
                return  
        print("Employee not found.")  

    def delete_employee(self, emp_id):  
        for employee in self.employees:  
            if employee.emp_id == emp_id:  
                self.employees.remove(employee)  
                print(f"Employee ID {emp_id} deleted successfully.")  
                return  
        print("Employee not found.")  


def main():  
    ems = EmployeeManagementSystem()  
    
    while True:  
        print("\nEmployee Management System")  
        print("1. Add Employee")  
        print("2. View Employees")  
        print("3. Update Employee")  
        print("4. Delete Employee")  
        print("5. Exit")  
        
        choice = input("Choose an option: ")  

        if choice == '1':  
            emp_id = input("Enter Employee ID: ")  
            name = input("Enter Name: ")  
            position = input("Enter Position: ")  
            department = input("Enter Department: ")  
            salary = float(input("Enter Salary: "))  
            ems.add_employee(emp_id, name, position, department, salary)  
        
        elif choice == '2':  
            ems.view_employees()  

        elif choice == '3':  
            emp_id = input("Enter Employee ID to update: ")  
            name = input("Enter new Name (leave blank to retain current): ")  
            position = input("Enter new Position (leave blank to retain current): ")  
            department = input("Enter new Department (leave blank to retain current): ")  
            salary = input("Enter new Salary (leave blank to retain current): ")  
            salary = float(salary) if salary else None  
            ems.update_employee(emp_id, name if name else None,  
                                position if position else None,  
                                department if department else None,  
                                salary)  

        elif choice == '4':  
            emp_id = input("Enter Employee ID to delete: ")  
            ems.delete_employee(emp_id)  

        elif choice == '5':  
            print("Exiting the Employee Management System.")  
            break  
        
        else:  
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":  
    main()
