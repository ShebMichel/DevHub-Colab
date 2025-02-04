import pandas as pd
import random

# Generate a list of employees with full details
def generate_employee_data(num_employees):
    employees = []
    for i in range(num_employees):
        employee = {
            "id": i + 1,
            "name": f"Employee {i + 1}",
            "age": random.randint(20, 60),
            "position": random.choice(["Manager", "Developer", "Designer", "Analyst", "HR"]),
            "salary": random.randint(30000, 120000),
            "email": f"employee{i + 1}@company.com"
        }
        employees.append(employee)
    return employees


# Input the total number of employee
Nbre_of_employees = int(input("Enter the total number of employees: "))
# Generate employee data
data = generate_employee_data(Nbre_of_employees)

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Let visualize the table before saving it into excel

print("The first 10 rows of the table")
print(df.head(10))

print("The last 5 rows of the table")
print(df.tail(10))

# Save to an Excel file
df.to_excel("employees.xlsx", index=False)

print("Employee data saved to employees.xlsx")