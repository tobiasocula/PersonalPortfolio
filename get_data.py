import yfinance as yf
from pathlib import Path

etf = yf.Ticker("CNYAN.MX")
df = etf.history(period="max", interval="1d")
df.to_csv(Path.cwd() / "data" / "OHCL" / "china.csv")