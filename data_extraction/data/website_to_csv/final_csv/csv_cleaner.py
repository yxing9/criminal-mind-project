import pandas as pd

# Load CSV file
df = pd.read_csv('killers_with_ordering.csv')

# Replace spaces in column headers with underscore
df.columns = df.columns.str.replace(' ', '_')

# Save the DataFrame back to a CSV file
df.to_csv('killers_cleaned.csv', index=False)
