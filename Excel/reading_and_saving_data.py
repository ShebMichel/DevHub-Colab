import random
import pandas as pd

num_employees = int(input("Enter the total number of employees: "))
employees = []
list_of_roles = ["Manager", "Developer", "Designer", "Analyst", "HR"]

for i in range(num_employees):
    employee = {
        "id": i + 1,
        "name": f"Employee {i + 1}",
        "age": random.randint(20, 60),
        "position": random.choice(list_of_roles),
        "salary": random.randint(30000, 120000),
        "email": f"employee{i + 1}@dmnsolutions.com.au"
    }
    if i==0:
    	employee['name']="michel"
    	employee['position']="Founder and Principal Consultant"
    	employee['email']=f"{employee['name']}@dmnsolutions.com.au"
    employees.append(employee)

# Convert to DataFrame
df = pd.DataFrame(employees)

# Save to Excel
df.to_excel("employees.xlsx", index=False)

print("Employee data has been saved to employees.xlsx")
