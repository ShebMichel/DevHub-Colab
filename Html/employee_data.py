from flask import Flask, render_template_string
import random

app = Flask(__name__)

# Generate a list of employees with full details
def generate_employee_data(num_employees=10):
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
        #print(employees)
    return employees

# Create a route to display employees in a table
@app.route('/')
def employee_table():
    employees = generate_employee_data()  # Generate a list of employees
    table_html = """
    <html>
        <head>
            <title>Employee List</title>
            <style>
                table {width: 80%; margin: 50px auto; border-collapse: collapse;}
                th, td {border: 1px solid #ddd; padding: 8px; text-align: center;}
                th {background-color: #f2f2f2;}
            </style>
        </head>
        <body>
            <h1 style="text-align:center;">Employee List</h1>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Position</th>
                    <th>Salary</th>
                    <th>Email</th>
                </tr>
                {% for employee in employees %}
                <tr>
                    <td>{{ employee.id }}</td>
                    <td>{{ employee.name }}</td>
                    <td>{{ employee.age }}</td>
                    <td>{{ employee.position }}</td>
                    <td>${{ employee.salary }}</td>
                    <td>{{ employee.email }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>
    """
    return render_template_string(table_html, employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
