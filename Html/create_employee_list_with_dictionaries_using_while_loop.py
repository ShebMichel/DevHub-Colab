
# Online Python - IDE, Editor, Compiler, Interpreter

import random
#import time
#def generate_employee_data(num_employees=10): = int(input("Enter the total number of employees: "))
num_employees = int(input("Enter the total number of employees: "))
listofemployees = []
list_of_roles =["Manager", "Developer", "Designer", "Analyst", "HR"]
#for i in range(num_employees):
i=0
while i<num_employees:
    print(i)
    employee = {
        "id": i + 1,
        "name": f"Employee {i + 1}",
        "age": random.randint(20, 60),
        "position": random.choice(list_of_roles),
        "salary": random.randint(30000, 120000),
        "email": f"employee{i + 1}@company.com"
    }
    print(f"employee_{i+1} is {employee}")
    listofemployees.append(employee)
    print(f"list of employees is {employee}")
    print("- "*30)
    input("Press Enter to continue...")
    i=i+1


