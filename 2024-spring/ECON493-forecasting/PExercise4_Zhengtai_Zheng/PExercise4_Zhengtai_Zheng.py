import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages

# Load the data
Zheng_Zhengtai_exercise3 = pd.read_excel("Zheng_Zhengtai_exercise3.xlsx")

# Ensure the date column is treated as a Date object
Zheng_Zhengtai_exercise3_cleaned = Zheng_Zhengtai_exercise3.copy()
Zheng_Zhengtai_exercise3_cleaned['date'] = pd.to_datetime(Zheng_Zhengtai_exercise3_cleaned['date'], format='%Y-%m-%d')

# Set up the plot for line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=Zheng_Zhengtai_exercise3_cleaned, x='date', y='iorb', label='IORB', color='blue', linestyle='--')
sns.lineplot(data=Zheng_Zhengtai_exercise3_cleaned, x='date', y='disct', label='Discount Rate', color='purple', linestyle='-.')
sns.lineplot(data=Zheng_Zhengtai_exercise3_cleaned, x='date', y='ffr', label='FFR', color='red', linestyle='-')
sns.lineplot(data=Zheng_Zhengtai_exercise3_cleaned, x='date', y='repo', label='Repo Rate', color='green', linestyle=':')

# Customize the plot
plt.title('Interest Rates Over Time')
plt.ylabel('Interest Rate (%)')
plt.xlabel('Date')
plt.legend(title='Rate Type', loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)
plt.grid(True)

# Prepare to save figures
pdf_pages = PdfPages('Interest_Rate_Plots.pdf')

# Save the current figure (line plot)
plt.tight_layout()
pdf_pages.savefig()

# Prepare the pie chart data
comparison = Zheng_Zhengtai_exercise3_cleaned['ffr'] > Zheng_Zhengtai_exercise3_cleaned['iorb']
above_count = comparison.sum()
below_count = (~comparison).sum()

plot_data = pd.DataFrame({
    'Condition': ['FFR Above IORB', 'FFR Below or Equal to IORB'],
    'Count': [above_count, below_count]
})

# Calculate percentages
total_counts = plot_data['Count'].sum()
plot_data['Percentage'] = plot_data['Count'] / total_counts * 100

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(plot_data['Percentage'], labels=plot_data['Condition'], colors=['red', 'steelblue'],
       autopct='%1.1f%%', startangle=90)
ax.axis('equal')

# Save the pie chart
plt.tight_layout()
pdf_pages.savefig(fig)
plt.close(fig)

# Close the PDF and finish up
pdf_pages.close()
