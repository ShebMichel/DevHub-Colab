
# Online Python - IDE, Editor, Compiler, Interpreter

import random
import time
#def generate_employee_data(num_employees=10): = int(input("Enter the total number of employees: "))
num_employees = int(input("Enter the total number of employees: "))
employees = []
list_of_roles =["Manager", "Developer", "Designer", "Analyst", "HR"]
for i in range(num_employees):
# i=0
# while i<=10:
    employee = {
        "id": i + 1,
        "name": f"Employee {i + 1}",
        "age": random.randint(20, 60),
        "position": random.choice(list_of_roles),
        "salary": random.randint(30000, 120000),
        "email": f"employee{i + 1}@company.com"
    }
    employees.append(employee)
    print(f"id={i+1} list of employees is {employees}")
    print("- "*30)
    input("Press Enter to continue...")
    #time.sleep(3)
    #return employees

