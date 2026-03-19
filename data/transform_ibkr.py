import pandas as pd
from pathlib import Path
print('HAHHAHA')
print(Path.cwd())

# Read the CSV, skipping the first two rows
df = pd.read_csv(
    Path.cwd() / "data" / "U12754443.TRANSACTIONS.20230912.20260316.csv",
    skiprows=2,  # Skip the first two rows
    header=None, # Do not use any row as header
)

# Manually set the column names based on the "Header" row
df.columns = [
    "Statement", "Type", "Date", "Account", "Description",
    "Transaction Type", "Symbol", "Quantity", "Price",
    "Price Currency", "Gross Amount", "Commission", "Net Amount"
]

# Drop the 'Account' and 'Description' columns
df = df.drop(columns=["Account", "Description"])

# Reset index for a clean DataFrame
df = df.reset_index(drop=True)

# Display the cleaned DataFrame
#print(df)
print(df["Gross Amount"])
print(df.columns)


df.to_csv(Path.cwd() / "data" / "IBKR_history.csv", index=False)