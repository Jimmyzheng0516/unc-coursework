
import pandas as pd

# Load data
a = pd.read_excel("DFF.xls", header=None)
b = pd.read_excel("DPCREDIT.xls", header=None)
c = pd.read_excel("IOER.xls", header=None)
d = pd.read_excel("IORB.xls", header=None)
e = pd.read_excel("RRPONTSYAWARD.xls", header=None)

def modify(z, label):
    # Find the starting row
    index_start = z[z.iloc[:, 0] == "observation_date"].index[0] + 1
    
    # Trim and rename columns
    z = z.iloc[index_start:]
    if z.shape[1] >= 2:
        z.columns = ["date", label]
        z["date"] = pd.to_datetime(z["date"])
    return z

# Process and rename
a = modify(a, "ffr")
b = modify(b, "disct")
c = modify(c, "x")
d = modify(d, "x")
e = modify(e, "repo")

# Combine IOER and IORB
d = pd.concat([c, d])
d.columns = ["date", "iorb"]

# Merge all dataframes
result = d.merge(b, on="date", how="left").merge(a, on="date", how="left").merge(e, on="date", how="left")

# Write to file
result.to_excel("Zheng_Zhengtai_exercise3.xlsx", index=False)
