
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from datetime import datetime

# Read data
data = pd.read_excel("Moderna_Pfizer Event Study.xlsx")

# Convert date
data['date'] = pd.to_datetime(data['Names Date'])

# Create Excess Returns
data['R_pfe'] = data['PFE'] - data['RF']
data['R_mrna'] = data['MRNA'] - data['RF']

# Training data for Pfizer
pfizer_data = data[(data['date'] >= pd.Timestamp('2019-01-01')) & (data['date'] <= pd.Timestamp('2020-12-03'))]

# Make sure Moderna has the equal training sample size
estim_window = len(pfizer_data)
moderna_end = pd.Timestamp('2020-12-10')
moderna_end_row = data[data['date'] == moderna_end].index[0]
moderna_start_row = moderna_end_row - estim_window + 1

# Training data for Moderna
moderna_data = data.iloc[moderna_start_row:moderna_end_row + 1]

# Run CAPM regressions
pfizer_capm = ols('R_pfe ~ Q("Mkt-RF")', data=pfizer_data).fit()
moderna_capm = ols('R_mrna ~ Q("Mkt-RF")', data=moderna_data).fit()

# Print the regression results
print("Pfizer CAPM Results:\n", pfizer_capm.summary())
print("\nModerna CAPM Results:\n", moderna_capm.summary())

# Define event windows
pfizer_event_start = pd.Timestamp('2020-12-04')
moderna_event_start = pd.Timestamp('2020-12-11')

# Filter event window data
pfizer_event_data = data[data['date'] >= pfizer_event_start]
moderna_event_data = data[data['date'] >= moderna_event_start]

# Calculate predicted returns using CAPM beta coefficients
pfizer_event_data['r_hat'] = pfizer_capm.predict(pfizer_event_data)
moderna_event_data['r_hat'] = moderna_capm.predict(moderna_event_data)

# Calculate abnormal returns
pfizer_event_data['ar'] = pfizer_event_data['R_pfe'] - pfizer_event_data['r_hat']
moderna_event_data['ar'] = moderna_event_data['R_mrna'] - moderna_event_data['r_hat']

# Print the first 20 AR's
print("First 20 AR's for Pfizer \n", pfizer_event_data['ar'].head(20))
print("First 20 AR's for Moderna \n", moderna_event_data['ar'].head(20))

# Calculate cumulative abnormal returns
pfizer_event_data['car'] = np.cumsum(pfizer_event_data['ar'])
moderna_event_data['car'] = np.cumsum(moderna_event_data['ar'])

# Days of interest
days_of_interest = [4, 9, 14, 19]

# Extract CAR values
pfizer_CAR_values = pfizer_event_data['car'].iloc[days_of_interest]
moderna_CAR_values = moderna_event_data['car'].iloc[days_of_interest]

# Print the cumulative abnormal returns
print("Cumulative Abnormal Returns for Pfizer:")
for i, days in enumerate(days_of_interest):
    print(f"CAR for {days+1} days: {pfizer_CAR_values.iloc[i]:.3f}")

print("\nCumulative Abnormal Returns for Moderna:")
for i, days in enumerate(days_of_interest):
    print(f"CAR for {days+1} days: {moderna_CAR_values.iloc[i]:.3f}")
