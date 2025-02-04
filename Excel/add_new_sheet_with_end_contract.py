import pandas as pd
import random
import os

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
            "email": f"employee{i + 1}@company.com",
            "contract_end": f"202{random.randint(3, 5)}-12-{random.randint(1, 28)}"  # Random contract end date
        }
        employees.append(employee)
    return employees

# Function to add a new sheet "Contract End"
def add_contract_end_sheet(file_name="employees.xlsx"):
    contract_data = generate_employee_data(Nbre_of_employees)  # Generate contract data
    
    # Convert data to DataFrame
    contract_df = pd.DataFrame(contract_data, columns=["id", "name", "position", "contract_end"])
    
    # Check if file exists
    if os.path.exists(file_name):
        with pd.ExcelWriter(file_name, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            contract_df.to_excel(writer, sheet_name="Contract End", index=False)
    else:
        with pd.ExcelWriter(file_name, mode="w", engine="openpyxl") as writer:
            contract_df.to_excel(writer, sheet_name="Contract End", index=False)
    
    print(f"Sheet 'Contract End' added to {file_name}")


# Input the total number of employee
Nbre_of_employees = int(input("Enter the total number of employees: "))

# Call function to add the new sheet
add_contract_end_sheet(Nbre_of_employees)
