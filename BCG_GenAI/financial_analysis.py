import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Extraction (Simulated)
# In a real scenario, you would use web scraping or APIs to extract data from SEC EDGAR
# For this example, we'll simulate the extracted data

companies = ['Microsoft', 'Tesla', 'Apple']
years = [2020, 2021, 2022]

data = {
    'Microsoft': {
        'Total Revenue': [143015, 168088, 198270],
        'Net Income': [44281, 61271, 72738],
        'Total Assets': [301311, 333779, 364840],
        'Total Liabilities': [183007, 193694, 198311],
        'Cash Flow from Operating Activities': [60675, 76740, 89035]
    },
    'Tesla': {
        'Total Revenue': [31536, 53823, 81462],
        'Net Income': [721, 5519, 12556],
        'Total Assets': [52148, 62131, 74918],
        'Total Liabilities': [28775, 30548, 36078],
        'Cash Flow from Operating Activities': [5943, 11497, 14724]
    },
    'Apple': {
        'Total Revenue': [274515, 365817, 394328],
        'Net Income': [57411, 94680, 99803],
        'Total Assets': [323888, 351002, 352755],
        'Total Liabilities': [258549, 287912, 302083],
        'Cash Flow from Operating Activities': [80674, 104038, 122151]
    }
}

# Create a DataFrame
df = pd.DataFrame(columns=['Company', 'Year', 'Metric', 'Value'])

for company in companies:
    for metric in data[company]:
        for i, year in enumerate(years):
            df = df.append({
                'Company': company,
                'Year': year,
                'Metric': metric,
                'Value': data[company][metric][i]
            }, ignore_index=True)

# Step 2: Data Analysis

def analyze_trend(company, metric):
    company_data = df[(df['Company'] == company) & (df['Metric'] == metric)]
    trend = company_data['Value'].pct_change().mean()
    return f"{company}'s {metric} {'increased' if trend > 0 else 'decreased'} by an average of {abs(trend)*100:.2f}% year-over-year."

def compare_companies(metric):
    plt.figure(figsize=(10, 6))
    for company in companies:
        company_data = df[(df['Company'] == company) & (df['Metric'] == metric)]
        plt.plot(company_data['Year'], company_data['Value'], marker='o', label=company)
    plt.title(f"Comparison of {metric}")
    plt.xlabel("Year")
    plt.ylabel("Value (in millions USD)")
    plt.legend()
    plt.savefig(f"{metric.replace(' ', '_')}_comparison.png")
    plt.close()

# Generate insights
insights = []
for company in companies:
    for metric in data[company]:
        insights.append(analyze_trend(company, metric))

# Compare companies
for metric in data[companies[0]]:
    compare_companies(metric)

# Print insights
print("Financial Insights:")
for insight in insights:
    print("- " + insight)

print("\nGraphs have been saved for each metric comparing the three companies.")

# Additional analysis: Profitability ratios
def calculate_profit_margin(company, year):
    revenue = df[(df['Company'] == company) & (df['Year'] == year) & (df['Metric'] == 'Total Revenue')]['Value'].values[0]
    net_income = df[(df['Company'] == company) & (df['Year'] == year) & (df['Metric'] == 'Net Income')]['Value'].values[0]
    return net_income / revenue

print("\nProfit Margins:")
for company in companies:
    for year in years:
        profit_margin = calculate_profit_margin(company, year)
        print(f"{company} ({year}): {profit_margin:.2%}")

# Save data to CSV for future use
df.to_csv('financial_data.csv', index=False)
print("\nFinancial data has been saved to 'financial_data.csv'")