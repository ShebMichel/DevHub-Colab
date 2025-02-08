# http://workshop.robin.com.au/chat/week3
import requests
import feedparser
import pprint

from flask import Flask, render_template_string
import random

app = Flask(__name__)
# the first of the call is to request the site/curl it
response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale', headers={'user-agent': ''})

#print(response.content)
#print('Done ')
############

# 2- Let parse the data

# response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale', headers={'user-agent': ''})

parse_data = feedparser.parse(response.content)
#print(f"parse data is:  {parse_data}")

# print('Done ')
# ####################
# #When you print out feed1, it looks like a mess, but you can try importing pprint and print out feed1 in a more formatted way. You can also print out the type of feed as follows:
# print('looking at pprint: ')
# pprint(parse_data)
# print('Done ')

## 
import pandas as pd 


df2 = pd.DataFrame()

for data_in_df, value in parse_data.items():
	#print(data_in_df,value)
	if str(data_in_df)=='entries':
		for entry in value:
			df1=pd.DataFrame([entry['location'],entry['price'],entry['address'] ]).T
			df2 =pd.concat([df2,df1],axis=0, ignore_index=True)
df2.columns =['Suburb', 'Price', 'Address']
# Create a route to display employees in a table
@app.route('/')
def employee_table():
    #employees = generate_employee_data()  # Generate a list of employees
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
                    <th>Suburb</th>
                    <th>Price</th>
                    <th>Adress</th>
                    <th>Position</th>
                    <th>Salary</th>
                    <th>Email</th>
                </tr>
                {% for employee in employees %}
                <tr>
                    <td>{{ employee.Suburb }}</td>
                    <td>{{ employee.Price }}</td>
                    <td>{{ employee.Address }}</td>
                    <td>{{ employee.position }}</td>
                    <td>${{ employee.salary }}</td>
                    <td>{{ employee.email }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>
    """
    return render_template_string(table_html, employees=df2)

if __name__ == '__main__':
    app.run(debug=True)

print(df2)
		

# Let now push it on website:





