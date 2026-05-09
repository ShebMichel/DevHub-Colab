import pandas as pd

# File path
file_path = 'statement1.xlsx'

# Read existing Excel file
df = pd.read_excel(file_path)

# Replace with your actual column name
column_name = 'Petrol'

# Create Petrol expense column
df['Petrol expense'] = df[column_name].astype(str).str.extract(r'(\d+)$').astype(float)

# Write back to the same Excel file as a NEW sheet
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, sheet_name='Processed_Data', index=False)

print("Done! Data saved in new sheet 'Processed_Data'")