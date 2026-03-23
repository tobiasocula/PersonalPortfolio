import pandas as pd
from pathlib import Path
import sys
# Load the data


# Read CSV files without setting index_col
snp = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com" / "CSPX ETF Stock Price History.csv")
china = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com" / "CNYA ETF Stock Price History.csv")
em = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com" / "EIMI ETF Stock Price History.csv")
gold = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com" / "XAD5 ETF Stock Price History.csv")
india = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com" / "INR ETF Stock Price History.csv")
mscieurope = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com" / "XMEU ETF Stock Price History.csv")
smallcapeurope = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com" / "SXRJ ETF Stock Price History.csv")

labels = [
    "CSPX ETF Stock Price History.csv",
    "CNYA ETF Stock Price History.csv",
    "EIMI ETF Stock Price History.csv",
    "XAD5 ETF Stock Price History.csv",
    "INR ETF Stock Price History.csv",
    "XMEU ETF Stock Price History.csv",
    "SXRJ ETF Stock Price History.csv"
]

import numpy as np
def clean_volume(vol_series):
    """Handle empty strings, NaN, K/M perfectly"""
    def parse_single(val):
        if pd.isna(val) or str(val).strip() == '' or str(val).lower() == 'nan':
            return np.nan
        val = str(val).strip().upper()
        if 'K' in val:
            return float(val.replace('K', '').replace(',', '')) * 1000
        elif 'M' in val:
            return float(val.replace('M', '').replace(',', '')) * 1_000_000
        else:
            return float(val.replace(',', ''))
    
    return vol_series.apply(parse_single)

dfs = [snp, china, em, gold, india, mscieurope, smallcapeurope]

# print("All volumes now float:", [df['Vol_clean'].dtype for df in dfs])
# print("Sample clean volumes:", dfs[0]['Vol_clean'].head())


dfs = [snp, china, em, gold, india, mscieurope, smallcapeurope]
dfs_new = []
for i, (label, df) in enumerate(zip(labels, dfs)):
    print('label:', label)
    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"])
     # Make sure these are strings first
    df["Price"] = df["Price"].astype(str).str.replace(",", "", regex=False)
    # Then to numeric, coercing bad values to NaN
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    print(f"DF {i} before: NaN count = {df['Vol.'].isna().sum()}")
    
    # Clean volume column
    df['Vol_clean'] = clean_volume(df['Vol.'])
    
    # Filter out NaN volumes AND NaN prices
    df_clean = df.dropna(subset=['Vol_clean', 'Price'])
    dfs[i] = df_clean  # Replace original
    
    print(f"DF {i} after: {len(df_clean)} rows, NaN vol = 0")
   
    dfs_new.append(df)

# Save the transformed DataFrame

for df, label in zip(dfs_new, labels):
    print('label:', label)
    df.to_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com_transformed" / label, index=False)
