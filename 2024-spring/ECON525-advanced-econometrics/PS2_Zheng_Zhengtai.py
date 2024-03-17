
import pandas as pd
import statsmodels.formula.api as smf


FAMA_Mcbeth = pd.read_excel("FAMA_Mcbeth.xlsx")

# Rename 'Mkt-RF' column to 'Mkt_RF'
FAMA_Mcbeth = FAMA_Mcbeth.rename(columns={'Mkt-RF': 'Mkt_RF'})

# Initialize a data frame to store 1st stage regression results
results_1st = pd.DataFrame(columns=['Portfolio', 'Alpha', 'Beta_Mkt', 'Beta_Inf', 'Beta_PCE', 'Adj_R2'])

# Run 25 regressions for the 1st stage
for i in range(1, 26):
    
    excess_R_it = FAMA_Mcbeth.iloc[:, i] - FAMA_Mcbeth['RF']  # Compute excess returns
    
    model = smf.ols(formula ='excess_R_it ~ Mkt_RF + CPIAUCSL_PCH + PCE_PCH', 
                    data=FAMA_Mcbeth.assign(excess_R_it=excess_R_it)).fit()
    
    results_1st = results_1st.append({'Portfolio': FAMA_Mcbeth.columns[i], 
                                      'Alpha': model.params[0], 
                                      'Beta_Mkt': model.params[1], 
                                      'Beta_Inf': model.params[2], 
                                      'Beta_PCE': model.params[3], 
                                      'Adj_R2': model.rsquared_adj}, 
                                     ignore_index=True)


# Calculate average returns for each portfolio
average_returns = FAMA_Mcbeth.iloc[:, 1:26].mean()

results_1st.reset_index(drop=True, inplace=True)
average_returns_df = average_returns.reset_index()
average_returns_df.columns = ['Portfolio', 'average_returns']

# Merge average_returns with Beta's in results_1st on Portfolio
data_2nd_reg = pd.merge(average_returns_df, results_1st, on='Portfolio')


# Run the 2nd stage regression with Newey-West standard errors
model_2nd = smf.ols('average_returns ~ Beta_Mkt + Beta_Inf + Beta_PCE', 
                    data=data_2nd_reg).fit(cov_type='HAC', cov_kwds={'maxlags':1})

print(model_2nd.summary())