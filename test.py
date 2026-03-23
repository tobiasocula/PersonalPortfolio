import pandas as pd
import numpy as np
from pathlib import Path
import plotly.graph_objects as go
from scipy.stats import multivariate_normal, norm

import numpy as np

snp = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com_transformed" / "CSPX ETF Stock Price History.csv")
china = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com_transformed" / "CNYA ETF Stock Price History.csv")
em = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com_transformed" / "EIMI ETF Stock Price History.csv")
gold = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com_transformed" / "XAD5 Historische Data.csv")
india = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com_transformed" / "INR ETF Stock Price History.csv")
mscieurope = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com_transformed" / "XMEU ETF Stock Price History.csv")
smallcapeurope = pd.read_csv(Path.cwd() / "data" / "OHCL" / "investing_dot_com_transformed" / "SXRJ ETF Stock Price History.csv")

print(snp["Vol_clean"].values)