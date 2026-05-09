import pandas as pd

# Read Excel file
df = pd.read_excel('statement1.xlsx')

# Inspect column names (optional but useful)
print(df.columns)

# Replace 'Fuel' with the actual column name in your file
column_name = 'Petrol'

# Create Petrol expense column
df['Petrol expense'] = df[column_name].astype(str).str.extract(r'(\d+)$').astype(float)

# Save updated file
df.to_excel('statement1_updated.xlsx', index=False)

print("Done! File saved as statement1_updated.xlsx")