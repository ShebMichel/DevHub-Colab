import pandas as pd
import random
import os
from openpyxl import load_workbook

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
def add_contract_end_sheet(Nbre_of_employees,file_name="employees.xlsx"):
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

# Function to prompt user for new employee details and append them to the "Contract End" sheet
def add_new_employee(file_name="employees.xlsx"):
    # Prompt user for details
    name = input("Enter Employee Name: ")
    position = input("Enter Employee Position: ")
    contract_end = input("Enter Contract End Date (YYYY-MM-DD): ")

    # Read the existing "Contract End" sheet
    if os.path.exists(file_name):
        try:
            existing_data = pd.read_excel(file_name, sheet_name="Contract End")
        except ValueError:
            existing_data = pd.DataFrame(columns=["id", "name", "position", "contract_end"])
    else:
        existing_data = pd.DataFrame(columns=["id", "name", "position", "contract_end"])

    # Determine new ID
    new_id = existing_data["id"].max() + 1 if not existing_data.empty else 1

    # Create new entry
    new_employee = pd.DataFrame([{
        "id": new_id,
        "name": name,
        "position": position,
        "contract_end": contract_end
    }])

    # Append new employee to the existing data
    updated_data = pd.concat([existing_data, new_employee], ignore_index=True)

    # Save back to Excel
    with pd.ExcelWriter(file_name, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        updated_data.to_excel(writer, sheet_name="Contract End", index=False)

    print(f"New employee '{name}' added to 'Contract End' sheet in {file_name}")



# Input the total number of employee
Nbre_of_employees = int(input("Enter the total number of employees: "))
# Example usage
add_contract_end_sheet(Nbre_of_employees)  # Create the sheet first
add_new_employee()  # Prompt user for input and append
