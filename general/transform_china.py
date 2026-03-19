import pandas as pd
from pathlib import Path

# Load the data
df = pd.read_csv(Path.cwd() / "data" / "OHCL" / "china.csv")

# Drop unnecessary columns
df = df.drop(columns=["Unnamed: 0", "Change %"])

# Rename columns
df = df.rename(columns={
    "Date": "Date",
    "Open": "Open",
    "High": "High",
    "Low": "Low",
    "Close": "Close",
    "Vol.": "Volume"
})

# Add missing columns with default values
df["Dividends"] = 0.0
df["Stock Splits"] = 0.0
df["Capital Gains"] = 0.0

# Parse 'Date' as datetime
df["Date"] = pd.to_datetime(df["Date"])

# Reorder columns
df = df[["Date", "Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits", "Capital Gains"]]

# Save the transformed DataFrame
df.to_csv(Path.cwd() / "data" / "OHCL" / "china_transformed.csv", index=False)
