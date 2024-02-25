

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.iolib.summary2 import summary_col

# Read the data
capm_data = pd.read_excel("CAPM.xlsx")

# Define the sizes of interest
sizes = [1, 2, 9, 10]

# Calculate excess returns for size and value portfolios
for i in sizes:
    size_col_name = f"size{i}"
    val_col_name = f"val{i}"
    capm_data[f"excess_{size_col_name}"] = capm_data[size_col_name] - capm_data['rf']
    capm_data[f"excess_{val_col_name}"] = capm_data[val_col_name] - capm_data['rf']

# Run CAPM regression with robust standard errors for size
results_size = []
for i in sizes:
    excess_size_col_name = f"excess_size{i}"
    model_size = smf.ols(formula=f"{excess_size_col_name} ~ rmrf", data=capm_data).fit(cov_type='HC0')
    results_size.append(model_size)

# Print results for size
print("Results for Size Portfolios:")
print(summary_col(results_size, stars=True))

# Run CAPM regression with robust standard errors for value
results_val = []
for i in sizes:
    excess_val_col_name = f"excess_val{i}"
    model_val = smf.ols(formula=f"{excess_val_col_name} ~ rmrf", data=capm_data).fit(cov_type='HC0')
    results_val.append(model_val)

# Print results for value
print("Results for Value Portfolios:")
print(summary_col(results_val, stars=True))

# Calculate SMB and HML factors
capm_data['SMB'] = capm_data['size1'] - capm_data['size10']
capm_data['HML'] = capm_data['val10'] - capm_data['val1']


# Fama-French three-factor model for size portfolios
results_ff_size = []
for i in sizes:
    excess_size_col_name = f"excess_size{i}"
    formula = f"{excess_size_col_name} ~ rmrf + SMB + HML"
    model_ff_size = smf.ols(formula=formula, data=capm_data).fit(cov_type='HC0')
    results_ff_size.append(model_ff_size)

# Print results for size portfolios
print("Results for Size Portfolios with Fama-French Three-Factor Model:")
print(summary_col(results_ff_size, stars=True))

# Fama-French three-factor model for value portfolios
results_ff_val = []
for i in sizes:
    excess_val_col_name = f"excess_val{i}"
    formula = f"{excess_val_col_name} ~ rmrf + SMB + HML"
    model_ff_val = smf.ols(formula=formula, data=capm_data).fit(cov_type='HC0')
    results_ff_val.append(model_ff_val)

# Print results for value portfolios
print("Results for Value Portfolios with Fama-French Three-Factor Model:")
print(summary_col(results_ff_val, stars=True))
