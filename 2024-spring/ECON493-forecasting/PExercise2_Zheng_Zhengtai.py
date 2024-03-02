
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Import Data
data_fama_french_factors = pd.read_excel("FAMA French 3 Factors monthly 2020.xlsx")

data_return = pd.read_excel("WMT-AAPL-MCD-return-data.xlsx") # cleaned data obtained from CRSP

# Create variables and delete unnecessary variables
data_fama_french_factors = data_fama_french_factors.drop(columns=data_fama_french_factors.columns[0])

data_return['date'] = pd.to_datetime(data_return['date']).dt.to_period('M')

data_fama_french_factors['date'] = data_return['date'].unique()

# Merge data
reg_data = pd.merge(data_return, data_fama_french_factors, on="date", how="left")

reg_data['excess_r_it'] = reg_data['r_it'] - reg_data['RF']

# Run the regression
firm_names = reg_data['ticker'].unique()

for i in firm_names:
    fama_french_model = smf.ols(formula='excess_r_it ~ Q("Mkt-RF") + SMB + HML', data=reg_data[reg_data['ticker'] == i]).fit()
    print(f"Results for {i}:\n")
    print(fama_french_model.summary())
    print("\n")
